import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config, browser
from utils import attach
from dotenv import load_dotenv
import os

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield browser


@pytest.fixture(scope="function", autouse=True)
def open_browser(setup_browser):
    browser = setup_browser
    browser.open('https://demoqa.com/automation-practice-form')
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")