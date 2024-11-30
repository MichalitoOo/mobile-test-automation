import logging

from Pages.home_page import HomePage
from Pages.login_page import LoginPage

# logger = logging.getLogger("test_logger")

# Static variable for valid login credentials
login_credentials = ("standard_user", "secret_sauce")


def test_add_to_cart(driver):
    """
    Objective: Verify that an item can be successfully added to the cart.

    Steps:
    1. Perform a valid login using predefined credentials.
    2. Verify login was successful.
    3. Retrieve the initial cart quantity.
    4. Add an item with a specific title to the cart using `add_to_cart`.
    5. Retrieve the updated cart quantity.
    6. Assert the cart quantity increases by 1.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    """
    login_page = LoginPage(driver)

    # Step 1: Perform valid login
    login_page.perform_login(*login_credentials)

    home_page = HomePage(driver)

    # Step 2: Verify login was successful
    assert home_page.is_logged_in(), "Login failed: Unable to access the home page."

    # Step 3: Retrieve the initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."

    # Step 4: Retrieve available items and add the first item to the cart
    items_available = home_page.get_available_items()
    assert items_available, "No items available to add to the cart."
    home_page.add_to_cart(items_available[0])

    # Step 5: Retrieve the updated cart quantity
    updated_quantity = home_page.get_cart_quantity()
    assert updated_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."

    # Step 6: Verify the cart quantity increased by 1
    assert updated_quantity == initial_quantity + 1, (
        f"Cart quantity did not increase as expected. "
        f"Expected: {initial_quantity + 1}, Got: {updated_quantity}."
    )


def test_remove_from_cart(driver):
    """
    Objective: Verify that an item can be successfully removed from the cart.

    Steps:
    1. Perform a valid login using predefined credentials.
    2. Verify login was successful.
    3. Retrieve available items and add an item to the cart using `add_to_cart`.
    4. Retrieve the initial cart quantity after adding the item.
    5. Remove the same item from the cart using `remove_from_cart`.
    6. Retrieve the updated cart quantity after removal.
    7. Assert the cart quantity decreases by 1.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    """
    login_page = LoginPage(driver)

    # Step 1: Perform valid login
    login_page.perform_login(*login_credentials)

    home_page = HomePage(driver)

    # Step 2: Verify login was successful
    assert home_page.is_logged_in(), "Login failed: Unable to access the home page."

    # Step 3: Retrieve available items and add the first item to the cart
    items_available = home_page.get_available_items()
    assert items_available, "No items available to add to the cart."
    home_page.add_to_cart(items_available[0])

    # Step 4: Retrieve the initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."

    # Step 5: Remove the same item from the cart
    home_page.remove_from_cart(items_available[0])

    # Step 6: Retrieve the updated cart quantity
    updated_quantity = home_page.get_cart_quantity()
    assert updated_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."

    # Step 7: Verify the cart quantity decreased by 1
    assert updated_quantity == initial_quantity - 1, (
        f"Cart quantity did not decrease as expected. "
        f"Expected: {initial_quantity - 1}, Got: {updated_quantity}."
    )
