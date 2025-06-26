import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from config.config import URL, USERNAME, INVALID_PASSWORD

@pytest.fixture
def driver():
    """Fixture to initialize and teardown WebDriver."""
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()


def perform_invalid_login_test(driver) -> bool:
    """Performs the login test and returns True if test passes, else False."""
    driver.get(URL)
    login_page = LoginPage(driver)
    login_page.login(USERNAME, INVALID_PASSWORD)
    error_msg = login_page.get_error_message()
    return "Epic sadface" in error_msg


def test_invalid_login(driver):
    """Pytest-compatible test using fixture."""
    assert perform_invalid_login_test(driver), "Expected error message not found."



