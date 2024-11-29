from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)  # Set default implicit wait timeout of 10 seconds


    def get_element(self, element):
        try:
            return self.driver.find_element(*element)
        except NoSuchElementException:
            return None

    def set_wait(self, timeout):
        self.driver.implicitly_wait(timeout)