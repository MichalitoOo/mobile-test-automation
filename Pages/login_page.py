from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from Pages.base_page import BasePage

class LoginPage(BasePage):
    """
    LoginPage handles interactions with the login screen of the application.
    It provides methods to perform login actions, verify login page presence,
    and check for error messages.
    """

    def __init__(self, driver):
        """
        Initialize the LoginPage.

        This constructor sets up the elements (username, password fields,
        and login button) that are used to interact with the login screen.

        :param driver: Appium WebDriver instance for interacting with the app.
        """
        super().__init__(driver)
        # Define locators for the username, password fields, and login button
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    def perform_login(self, username: str, password: str):
        """
        Perform a login attempt using the provided username and password.

        This method clears any pre-filled values in the username and password
        fields, enters the provided credentials, and clicks the login button.

        :param username: The username to input into the login form.
        :param password: The password to input into the login form.
        """
        # Clear and fill in the username field
        username_field = self.driver.find_element(*self.username_field)
        username_field.clear()
        username_field.send_keys(username)

        # Clear and fill in the password field
        password_field = self.driver.find_element(*self.password_field)
        password_field.clear()
        password_field.send_keys(password)

        # Click the login button to attempt login
        self.driver.find_element(*self.login_button).click()

    def is_on_login_page(self):
        """
        Check if the current page is the login page.

        This method verifies that the login page is displayed by checking if
        the login button is present and visible on the screen.

        :return: True if login page is loaded and login button is visible, False otherwise.
        """
        login_button = self.get_element(self.login_button)
        return login_button is not None and login_button.is_displayed()

    def is_error_message_present(self, text: str) -> bool:
        """
        Check if an error message with the given text is displayed on the screen.

        This method searches for a TextView element that matches the provided
        error message and verifies if it is displayed.

        :param text: The exact text of the error message to look for.
        :return: True if the error message is found and displayed, False otherwise.
        """
        try:
            # Locate the error message by its exact text
            error_message = self.driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')
            return error_message.is_displayed()
        except NoSuchElementException:
            return False
