from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from Pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    def perform_login(self, username, password):
        # Perform login
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_error_message_present(self, text):
        try:
            return self.driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]').is_displayed()
        except NoSuchElementException:
            return False
