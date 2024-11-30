from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
import logging

logger = logging.getLogger("test_logger")  # Debug logger (if needed)


class HomePage(BasePage):
    """
    HomePage encapsulates interactions with the main screen of the application after login.
    It provides methods to interact with items, the cart, and other elements on the home page.
    """

    def __init__(self, driver):
        """
        Initialize the HomePage.

        :param driver: Appium WebDriver instance for interacting with the app.
        """
        super().__init__(driver)
        self.inventory_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')

    def add_to_cart(self, item_title: str):
        """
        Add an item to the cart by its title.

        :param item_title: The title of the item to add to the cart.
        :raises: NoSuchElementException if the "ADD TO CART" button is not found.
        """
        # Generate the XPath for the "ADD TO CART" button of the specific item
        add_button_xpath = self.get_item_button_xpath(item_title, button_type="ADD TO CART")
        add_button = self.driver.find_element(AppiumBy.XPATH, add_button_xpath)

        # Click the "ADD TO CART" button
        add_button.click()

    def remove_from_cart(self, item_title: str):
        """
        Remove an item from the cart by its title.

        :param item_title: The title of the item to remove from the cart.
        :raises: NoSuchElementException if the "REMOVE" button is not found.
        """
        # Generate the XPath for the "REMOVE" button of the specific item
        remove_button_xpath = self.get_item_button_xpath(item_title, button_type="REMOVE")
        remove_button = self.driver.find_element(AppiumBy.XPATH, remove_button_xpath)

        # Click the "REMOVE" button
        remove_button.click()

    def get_cart_quantity(self) -> int | None:
        """
        Retrieve the quantity of items in the cart.

        :return:
            - An integer representing the quantity if found.
            - 0 if the cart icon is present but no items are in it.
            - None if the cart icon is not found, or if quantity contains unexpected characters.
        """
        cart_present = None  # Placeholder to track cart presence
        try:
            cart_present = self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]')
            cart_quantity = self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]//android.widget.TextView').get_attribute("text")
            if cart_quantity.isdigit():
                return int(cart_quantity)  # Valid cart quantity
            else:
                return None  # Unexpected characters in cart quantity
        except NoSuchElementException:
            if cart_present:
                return 0  # Cart is present but no items yet
            else:
                return None  # Cart icon not present

    def is_logged_in(self):
        """
        Verifies if the user is logged in by checking the visibility of the inventory title.

        Returns:
            bool: True if the user is on the home screen, False otherwise.
        """
        try:
            element = self.get_element(self.inventory_title)
            return element is not None and element.is_displayed()
        except NoSuchElementException:
            return False

    def get_available_items(self) -> list[str] | None:
        """
        Get the titles of all available items on the home page.

        :return:
            - A list of item titles if found.
            - None if no items are available.
        """
        try:
            items = self.driver.find_elements(By.XPATH, '//android.view.ViewGroup[@content-desc="test-Item"]')
            # log the number of items found
            logger.info(f"Number of items found: {len(items)}")
            titles = []
            for item in items:
                # log the title of each item found
                try:
                    item_title = item.find_element(By.XPATH,
                                                   './/android.widget.TextView[@content-desc="test-Item title"]').get_attribute('text')
                    logger.info(f"Item title: {item_title}")
                    titles.append(item_title)
                except NoSuchElementException:
                    pass
            return titles
        except NoSuchElementException:
            return None

    @staticmethod
    def get_item_button_xpath(item_title: str, button_type: str) -> str:
        """
        Generate the XPath for a button ('ADD TO CART' or 'REMOVE') corresponding to the given item title.

        :param item_title: The title of the item.
        :param button_type: The type of button ('ADD TO CART' or 'REMOVE').
        :return: The constructed XPath for the specified button.
        """
        return f'//android.widget.TextView[@content-desc="test-Item title" and @text="{item_title}"]' \
               f'/following-sibling::android.view.ViewGroup[@content-desc="test-{button_type}"]'
