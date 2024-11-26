from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
        self.error_message = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Sorry')]")

    def perform_login(self, username, password):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except NoSuchElementException:
            return None
