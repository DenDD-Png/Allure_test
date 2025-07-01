from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from selenium.webdriver.remote.remote_connection import ClientConfig
from utils import attach



@pytest.fixture(scope="function", autouse=True)
def open_browser(setup_browser):
    browser = setup_browser
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()

@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    config = ClientConfig()
    config.keep_alive = True

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )


    browser = Browser(Config(driver))
    yield browser
    browser.quit()