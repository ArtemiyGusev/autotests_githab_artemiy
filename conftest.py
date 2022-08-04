import os

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core import driver

from utils import attach
from selene import Browser, Config

'''
Есть переменная называемая Hook
'''
chrome_only = pytest.mark.parametrize("browser_select", ["Chrome"], indirect=True)


@pytest.fixture(params=["Chrome", "Firefox"])
def browser_select(request):
    return request.param + " from fixture"


@pytest.fixture(scope='function', autouse=True)
def driver_init():
    browser.config.base_url = 'https://github.com'

    browser_config = browser.config

    yield browser_config

    attach.add_attachment(browser_config)
    attach.add_logs(browser_config)
    attach.add_html(browser_config)
    attach.add_video(browser_config)

    browser.quit()
