import pytest
import logging

from Pages.home_page import HomePage
from Pages.login_page import LoginPage


#logger = logging.getLogger("test_logger") # debug
#--STATIC VARIABLE--#
login_credentials = ("standard_user", "secret_sauce")


def test_add_to_cart(driver):
    """
    Objective: Verify that an item can be successfully added to the cart.
    Steps:
        1. Add an item with a specific title to the cart using add_to_cart.
        2. Assert the cart quantity increases by 1.

    :param driver:
    :return:
    """
    login_page = LoginPage(driver)
    # Perform valid login
    login_page.perform_login(*login_credentials)

    home_page = HomePage(driver)
    items_available = home_page.get_available_items()

    # Step 1: Retrieve initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."

    # Step 2: Add an item to the cart
    home_page.add_to_cart(items_available[0])

    # Step 3: Retrieve updated cart quantity
    updated_quantity = home_page.get_cart_quantity()
    assert updated_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    assert updated_quantity == initial_quantity + 1, f"Cart quantity did not increase as expected. Expected: {initial_quantity + 1}, Got: {updated_quantity}."


def test_remove_from_cart(driver):
    """
    Objective: Verify that an item can be successfully removed from the cart.
    Steps:
        1. Ensure an item is in the cart using add_to_cart.
        2. Remove the same item using remove_from_cart.
        3. Assert the cart quantity decreases by 1.

    :param driver:
    :return:
    """
    login_page = LoginPage(driver)
    # Perform valid login
    login_page.perform_login(*login_credentials)
    home_page = HomePage(driver)
    items_available = home_page.get_available_items()
    home_page.add_to_cart(items_available[0])
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    home_page.remove_from_cart(items_available[0])
    updated_quantity = home_page.get_cart_quantity()
    assert updated_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    assert updated_quantity == initial_quantity - 1, f"Cart quantity did not increase as expected. Expected: {initial_quantity - 1}, Got: {updated_quantity}."