from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')

    def add_to_cart(self, item_title):
        # Find the corresponding "ADD TO CART" button for the specific item title
        add_button_xpath = self.get_item_button_xpath(item_title, button_type="ADD TO CART")
        add_button = self.driver.find_element(AppiumBy.XPATH, add_button_xpath)

        # Click the "ADD TO CART" button
        add_button.click()


    def remove_from_cart(self, item_title):
        # Find the corresponding "REMOVE" button for the specific item title
        remove_button_xpath = self.get_item_button_xpath(item_title, button_type="REMOVE")
        remove_button = self.driver.find_element(AppiumBy.XPATH, remove_button_xpath)

        # Click the "REMOVE" button
        remove_button.click()

    def get_cart_quantity(self):
        cart_present = None # placeholder
        try:
            cart_present = self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]')
            cart_quantity = self.driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]//android.widget.TextView').get_attribute("text")
            if cart_quantity.isdigit():
                return int(cart_quantity)   # valid number
            else:
                return None                 # unexpected char representing cart quantity
        except NoSuchElementException:
            if cart_present:
                return 0                    # Cart present but nothing is in it yet - no number in the icon.
            else:
                return None                 # Cart not present at all

    def get_available_items(self):
        try:
            items = self.driver.find_elements(By.XPATH, '//android.view.ViewGroup[@content-desc="test-Item"]')
            titles = []
            for item in items:
                titles.append(item.find_element(By.XPATH, './/android.widget.TextView[@content-desc="test-Item title"]').get_attribute("text"))
            return titles
        except NoSuchElementException:
            return None

    # helper function for code reusability
    @staticmethod
    def get_item_button_xpath(item_title, button_type):
        """
         Generate the XPath for the desired button ('ADD TO CART' or 'REMOVE') for the given item title.
        """
        return f'//android.widget.TextView[@content-desc="test-Item title" and @text="{item_title}"]' \
               f'/following-sibling::android.view.ViewGroup[@content-desc="test-{button_type}"]'