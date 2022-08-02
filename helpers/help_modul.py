import os

from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def url_open_size(url='', width=1920, height=1080):
    browser.config.browser_name = 'chrome'
    browser.open(url)
    browser.config.driver.set_window_size(width, height)