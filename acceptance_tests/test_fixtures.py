import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s

from conftest import firefox_only


def test_one(desktop_only):
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()


@firefox_only
def test_one_mobile(mobile_only):
    allure.dynamic.tag("Web application mobile")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Клик по кнопке бару'):
        s('[class="octicon octicon-three-bars"]').click()

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()
