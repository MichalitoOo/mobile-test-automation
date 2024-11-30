from selenium.common.exceptions import NoSuchElementException

class BasePage:
    """
    BasePage serves as the foundation for all page objects.
    It provides reusable methods and common functionality to interact with the mobile application.
    """

    def __init__(self, driver, timeout: int = 10):
        """
        Initialize the BasePage.

        :param driver: Appium WebDriver instance for interacting with the app.
        :param timeout: Default implicit wait timeout in seconds. Defaults to 10 seconds if not provided.
        """
        self.driver = driver
        self.driver.implicitly_wait(timeout)  # Configure the implicit wait timeout.

    def get_element(self, element):
        """
        Locate a single element on the page.

        :param element: A tuple containing the locator strategy and the locator selector
                        (e.g., (By.XPATH, '//element_xpath')).
        :return: The located element if found, or None if the element is not found.
        """
        try:
            return self.driver.find_element(*element)
        except NoSuchElementException:
            return None

    def set_wait(self, timeout: int):
        """
        Adjust the implicit wait timeout for the driver.

        :param timeout: The duration (in seconds) to set as the new implicit wait timeout.
        """
        self.driver.implicitly_wait(timeout)
