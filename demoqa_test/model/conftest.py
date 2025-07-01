import pytest
from selene import browser
import allure


@pytest.fixture(scope="function", autouse=True)
def open_browser1():
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()