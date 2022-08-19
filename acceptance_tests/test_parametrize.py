import pytest
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s

from conftest import chrome_only
from helpers.help_modul import url_open_size


@pytest.fixture()
def browser_permission(request):
    permission = {'desktop': (1920, 1366), 'mobile': (800, 600)}
    return permission[request.param]


@pytest.mark.parametrize("browser_permission", {"desktop"}, indirect=True)
def test_one(browser_permission):
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем github.com'):
        url_open_size(permission=browser_permission)

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()


@chrome_only
@pytest.mark.parametrize("browser_permission", {"mobile"}, indirect=True)
def test_one_mobile(browser_permission):
    allure.dynamic.tag("Web application mobile")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем github.com'):
        url_open_size(permission=browser_permission)

    with allure.step('Клик по кнопке бару'):
        s('[class="octicon octicon-three-bars"]').click()

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()
