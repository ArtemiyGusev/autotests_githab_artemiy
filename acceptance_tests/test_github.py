import pytest
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s, ss

from conftest import chrome_only, firefox_only
from helpers.help_modul import url_open_size


@chrome_only
@pytest.mark.parametrize("width, height",
                         [
                             pytest.param(1920, 1366),
                             pytest.param(1366, 768, marks=[pytest.mark.xfail(reason="Не валидное разрешение")]),
                             pytest.param(800, 600, marks=[pytest.mark.skip(reason="В процессе разработки")])
                         ]
                         )
def test_one(width, height):
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем github.com'):
        url_open_size(width, height)

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()


@firefox_only
def test_two():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем github.com'):
        url_open_size()

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()