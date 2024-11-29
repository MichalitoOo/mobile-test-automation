import pytest
from appium.webdriver.common.appiumby import AppiumBy
import logging

from Pages.home_page import HomePage
from Pages.login_page import LoginPage

#logger = logging.getLogger("test_logger") # debug

# Test for a valid login
def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Ensure login page
    login_button = login_page.get_element(login_page.login_button)
    assert login_button.is_displayed(), "Login page not loaded: Login button si not displayed"

    # Perform valid login
    login_page.perform_login("standard_user", "secret_sauce")

    # Ensure home page - login was successful
    home_page = HomePage(driver)
    inventory_title = home_page.get_element(home_page.inventory_title)
    assert inventory_title.is_displayed(), "Home page not loaded: Inventory screen is not displayed after login!"



@pytest.mark.parametrize("username, password, expected_message",
    [
        ("standard_user",   "",                     "Password is required"),
        ("",                "invalid_password",     "Username is required"),
        ("",                "",                     "Username is required"),
        ("standard_user",    "invalid_password",    "Username and password do not match any user in this service."),
        ("locked_out_user", "secret_sauce",         "Sorry, this user has been locked out."),                           # Locked out user
        ("invalid_user",    "invalid_password",     "Username and password do not match any user in this service.")    # Invalid login
    ]
)
def test_invalid_login(driver, username, password, expected_message):
    login_page = LoginPage(driver)

    login_page.perform_login(username, password)
    assert login_page.is_error_message_present(expected_message), f"Expected error message '{expected_message}' not present"

