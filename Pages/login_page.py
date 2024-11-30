from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from Pages.base_page import BasePage


class LoginPage(BasePage):
    """
    LoginPage handles interactions with the login screen of the application.
    It provides methods to perform login actions and verify error messages.
    """

    def __init__(self, driver):
        """
        Initialize the LoginPage.

        :param driver: Appium WebDriver instance for interacting with the app.
        """
        super().__init__(driver)
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    def perform_login(self, username: str, password: str):
        """
        Perform a login attempt using the provided username and password.

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

        # Click the login button
        self.driver.find_element(*self.login_button).click()

    def is_error_message_present(self, text: str) -> bool:
        """
        Check if an error message with the given text is displayed on the screen.

        :param text: The exact text of the error message to look for.
        :return: True if the error message is found and displayed, False otherwise.
        """
        try:
            error_message = self.driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')
            return error_message.is_displayed()
        except NoSuchElementException:
            return False
