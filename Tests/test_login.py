import pytest
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
import os

# Test for a valid login
def test_valid_login(driver):
    """
    Test the login functionality with valid credentials.

    Steps:
    1. Verify the login page is displayed.
    2. Perform login using valid credentials (username: 'standard_user', password: 'secret_sauce').
    3. Verify the home page is displayed after successful login.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    :raises AssertionError: If the login page is not displayed, login fails, or home page is not displayed after login.
    """

    # Fetch credentials from environment variables
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    # Ensure credentials are set
    assert username is not None, "TEST_USERNAME environment variable is not set."
    assert password is not None, "TEST_PASSWORD environment variable is not set."

    login_page = LoginPage(driver)

    # Step 1: Ensure login page is loaded
    login_button = login_page.get_element(login_page.login_button)
    assert login_button is not None and login_button.is_displayed(), \
        "Login page not loaded: Login button is not displayed."

    # Step 2: Perform valid login
    login_page.perform_login("standard_user", "secret_sauce")

    # Step 3: Ensure home page is loaded
    home_page = HomePage(driver)
    assert home_page.is_logged_in(), "Home page not loaded: User is not logged in."


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("standard_user",   "",                  "Password is required"),
        ("",                "invalid_password",  "Username is required"),
        ("",                "",                  "Username is required"),
        ("standard_user",   "invalid_password",  "Username and password do not match any user in this service."),
        ("locked_out_user", "secret_sauce",      "Sorry, this user has been locked out."),  # Locked out user
        ("invalid_user",    "invalid_password",  "Username and password do not match any user in this service.")  # Invalid login
    ]
)
def test_invalid_login(driver, username, password, expected_message):
    """
    Test the login functionality with invalid credentials.

    Steps:
    1. Verify the login page is displayed.
    2. Perform login using the provided username and password.
    3. Verify the expected error message is displayed.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    :param username: The username to use for login.
    :param password: The password to use for login.
    :param expected_message: The expected error message to verify.
    """
    login_page = LoginPage(driver)

    # Step 1: Ensure login page is loaded
    login_button = login_page.get_element(login_page.login_button)
    assert login_button is not None and login_button.is_displayed(), \
        "Login page not loaded: Login button is not displayed."

    # Step 2: Perform login with invalid credentials
    login_page.perform_login(username, password)

    # Step 3: Verify the expected error message is displayed
    assert login_page.is_error_message_present(expected_message), \
        f"Expected error message '{expected_message}' not present."
