import os
import pytest
from selene.support.shared import browser
from utils import attach


chrome_only = pytest.mark.parametrize("browser_select", ["chrome"], indirect=True)

firefox_only = pytest.mark.parametrize("browser_select", ["firefox"], indirect=True)


'''
На каких браузерах запускаются тесты
'''
@pytest.fixture(params=["chrome", "firefox"])
def browser_select(request):
    return request.param


@pytest.fixture(scope='function', autouse=True)
def driver_init(browser_select):

    os.environ['GH_TOKEN'] = "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"

    browser.config.browser_name = browser_select
    browser.config.base_url = 'https://github.com'

    browser_config = browser.config

    yield browser_config

    attach.add_attachment(browser_config)
    attach.add_html(browser_config)
    attach.add_video(browser_config)

    browser.quit()
