import os

import allure
import pytest
from selene.support.shared import browser

from helpers.help_modul import url_open_size
from utils import attach
from dotenv import load_dotenv


@pytest.fixture()
def desktop_only():
    with allure.step('Открываем github.com'):
        url_open_size()


@pytest.fixture()
def mobile_only():
    with allure.step('Открываем github.com'):
        url_open_size(600, 800)


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


chrome_only = pytest.mark.parametrize("browser_select", ["chrome"], indirect=True)
firefox_only = pytest.mark.parametrize("browser_select", ["firefox"], indirect=True)


@pytest.fixture(params=["chrome", "firefox"])
def browser_select(request):
    return request.param


@pytest.fixture(scope='function', autouse=True)
def driver_init(browser_select):

    #Лучше спрятать куда-нибудь, но для дз сойдет
    os.environ['GH_TOKEN'] = os.getenv('token')

    browser.config.browser_name = browser_select
    browser.config.base_url = 'https://github.com'

    browser_config = browser.config

    yield browser_config

    attach.add_attachment(browser_config)
    attach.add_html(browser_config)
    attach.add_video(browser_config)

    browser.quit()
