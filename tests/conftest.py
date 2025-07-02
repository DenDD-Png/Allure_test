import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config, browser
from utils import attach
from dotenv import load_dotenv
import os

@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableLog": True,
            "enableVideo": True,
            "sessionTimeout": "5m"
        }
    }

    options.capabilities.update(capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


#@pytest.fixture(scope="function", autouse=True)
#def open_browser():
    #browser.open('https://demoqa.com/automation-practice-form')
    #yield
    #browser.quit()


