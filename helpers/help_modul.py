from selene.support.shared import browser


def url_open_size(width=1920, height=1080, url=''):
    browser.open(url)
    browser.config.driver.set_window_size(width, height)