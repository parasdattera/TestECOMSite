import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config.config import URL, USERNAME, PASSWORD, INVALID_PASSWORD

def test_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    login = LoginPage(driver)
    login.login(USERNAME, INVALID_PASSWORD)
    assert "Epic sadface" in login.get_error_message()
    driver.quit()