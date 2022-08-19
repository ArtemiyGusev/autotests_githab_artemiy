from selene.support.shared import browser


def url_open_size(width=1920, height=1080, url='', permission=None):
    browser.open(url)
    if permission is not None:
        width = permission[0]
        height = permission[1]
    browser.config.driver.set_window_size(width, height)
