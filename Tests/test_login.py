import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Pages.login_page import LoginPage

# Test for a valid login
def test_valid_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.perform_login("standard_user", "secret_sauce")

    # Assert successful login by checking if the inventory screen is displayed
    inventory_title = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Inventory")
    assert inventory_title.is_displayed(), "Inventory screen is not displayed after login!"


@pytest.mark.parametrize("username, password, expected_message", [
    ("", "invalid_password", "Username is required"),                                                       # Missing username
    ("invalid_user", "", "Password is required"),                                                           # Missing password
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),                           # Locked out user
    ("invalid_user", "invalid_password", "Username and password do not match any user in this service.")    # Invalid login
])
def test_invalid_login(driver, username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.perform_login(username, password)
    error_message = login_page.get_error_message()
    assert error_message == expected_message, f"Expected error message '{expected_message}', got '{error_message}'"
