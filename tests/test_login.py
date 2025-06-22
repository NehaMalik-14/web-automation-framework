import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.wait_helper import WaitHelper

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://example.com/login")  # replace later
    yield driver
    driver.quit()

def test_login_flow(driver):
    login_page = LoginPage(driver)
    login_page.login("testuser", "testpass")

    # TODO: Add assertion when actual app is used
    assert driver.current_url != ""
