import time

import allure
import pytest
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s, ss
from helpers.help_modul import url_open_size



def test_one():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем github.com'):
        url_open_size()

    with allure.step('Клик по кнопке Sign in'):
        s('[href="/login"]').click()

