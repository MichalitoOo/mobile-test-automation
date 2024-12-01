import logging
import os
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
import time
import pytest

logger = logging.getLogger(__name__)

@pytest.mark.order(3)
def test_add_to_cart(driver):
    """
    Objective: Verify that an item can be successfully added to the cart.

    Steps:
    1. Perform a valid login using credentials from environment variables.
    2. Verify login was successful.
    3. Retrieve the initial cart quantity.
    4. Add an item with a specific title to the cart using `add_to_cart`.
    5. Retrieve the updated cart quantity.
    6. Assert the cart quantity increases by 1.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    """

    # Fetch credentials from environment variables
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    # Ensure credentials are set
    assert username is not None, "TEST_USERNAME environment variable is not set."
    assert password is not None, "TEST_PASSWORD environment variable is not set."
    logger.info("Credentials fetched from environment variables.")

    login_page = LoginPage(driver)

    # Step 1: Ensure login page is loaded and perform valid login
    assert login_page.is_on_login_page(), "Login page not loaded: Login form is not displayed."
    login_page.perform_login(username, password)
    logger.info("Login performed successfully.")

    home_page = HomePage(driver)

    # Step 2: Verify login was successful
    assert home_page.is_logged_in(), "Login failed: Unable to access the home page."
    logger.info("Login verified, user is on the home page.")

    # Step 3: Retrieve the initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    logger.info(f"Initial cart quantity retrieved: {initial_quantity}")

    # Step 4: Retrieve available items and add the first item to the cart
    items_available = home_page.get_available_items()
    assert items_available, "No items available to add to the cart."
    logger.info(f"Available items retrieved: {len(items_available)} items found.")
    home_page.add_to_cart(items_available[0])
    logger.info(f"Item {items_available[0]} added to the cart.")

    # Step 5: Retrieve the updated cart quantity
    updated_quantity = home_page.get_cart_quantity()
    assert updated_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    logger.info(f"Updated cart quantity retrieved: {updated_quantity}")

    # Step 6: Verify the cart quantity increased by 1
    assert updated_quantity == initial_quantity + 1, (
        f"Cart quantity did not increase as expected. "
        f"Expected: {initial_quantity + 1}, Got: {updated_quantity}."
    )
    logger.info(f"Test passed: Cart quantity increased by 1.")

@pytest.mark.order(4)
def test_remove_from_cart(driver):
    """
    Objective: Verify that an item can be successfully removed from the cart.

    Steps:
    1. Perform a valid login using credentials from environment variables.
    2. Verify login was successful.
    3. Retrieve available items and add an item to the cart using `add_to_cart`.
    4. Retrieve the initial cart quantity after adding the item.
    5. Remove the same item from the cart using `remove_from_cart`.
    6. Retrieve the updated cart quantity after removal.
    7. Assert the cart quantity decreases by 1.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    """

    # Fetch credentials from environment variables
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    # Ensure credentials are set
    assert username is not None, "TEST_USERNAME environment variable is not set."
    assert password is not None, "TEST_PASSWORD environment variable is not set."
    logger.info("Credentials fetched from environment variables.")

    login_page = LoginPage(driver)

    # Step 1: Ensure login page is loaded and perform valid login
    assert login_page.is_on_login_page(), "Login page not loaded: Login form is not displayed."
    login_page.perform_login(username, password)
    logger.info("Login performed successfully.")

    home_page = HomePage(driver)

    # Step 2: Verify login was successful
    assert home_page.is_logged_in(), "Login failed: Unable to access the home page."
    logger.info("Login verified, user is on the home page.")

    # Step 3: Retrieve available items and add the first item to the cart
    items_available = home_page.get_available_items()
    assert items_available, "No items available to add to the cart."
    logger.info(f"Available items retrieved: {len(items_available)} items found.")
    home_page.add_to_cart(items_available[0])
    logger.info(f"Item {items_available[0]} added to the cart.")

    # Step 4: Retrieve the initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    logger.info(f"Initial cart quantity retrieved: {initial_quantity}")

    # Step 5: Remove the same item from the cart
    home_page.remove_from_cart(items_available[0])
    logger.info(f"Item {items_available[0]} removed from the cart.")

    # Step 6: Retrieve the updated cart quantity
    updated_quantity = home_page.get_cart_quantity()
    assert updated_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    logger.info(f"Updated cart quantity retrieved: {updated_quantity}")

    # Step 7: Verify the cart quantity decreased by 1
    assert updated_quantity == initial_quantity - 1, (
        f"Cart quantity did not decrease as expected. "
        f"Expected: {initial_quantity - 1}, Got: {updated_quantity}."
    )
    logger.info(f"Test passed: Cart quantity decreased by 1.")

@pytest.mark.order(5)
def test_add_and_remove_same_item_multiple_times(driver, cycles = 5):
    """
    Objective: Ensure the cart count updates correctly when the same item is added and removed multiple times.

    Steps:
    1. Perform a valid login using credentials from environment variables.
    2. Verify login was successful.
    3. Retrieve the initial cart quantity.
    4. Add and remove the same item in multiple cycles.
    5. Verify the cart count resets to its initial value after each cycle.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    :param cycles: The number of cycles to repeat the add/remove operation. By default, set to 5 cycles.
    """

    # Fetch credentials from environment variables
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    # Ensure credentials are set
    assert username is not None, "TEST_USERNAME environment variable is not set."
    assert password is not None, "TEST_PASSWORD environment variable is not set."
    logger.info("Credentials fetched from environment variables.")

    login_page = LoginPage(driver)

    # Step 1: Ensure login page is loaded and perform valid login
    assert login_page.is_on_login_page(), "Login page not loaded: Login form is not displayed."
    login_page.perform_login(username, password)
    logger.info("Login performed successfully.")

    home_page = HomePage(driver)

    # Step 2: Verify login was successful
    assert home_page.is_logged_in(), "Login failed: Unable to access the home page."
    logger.info("Login verified, user is on the home page.")

    # Step 3: Retrieve the initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    logger.info(f"Initial cart quantity retrieved: {initial_quantity}")

    # Step 4: Retrieve available items
    items_available = home_page.get_available_items()
    assert items_available, "No items available to add to the cart."
    logger.info(f"Available items retrieved: {len(items_available)} items found.")

    # Select the first item to add and remove in cycles
    item_to_test = items_available[0]

    # Step 5: Perform add and remove in cycles
    for cycle in range(1, cycles + 1):
        logger.info(f"Starting cycle {cycle}.")

        # Add the item to the cart
        home_page.add_to_cart(item_to_test)
        logger.info(f"Item {item_to_test} added to the cart in cycle {cycle}.")

        # Verify cart count increased by 1
        updated_quantity = home_page.get_cart_quantity()
        assert updated_quantity == initial_quantity + 1, (
            f"Cycle {cycle}: Cart quantity did not increase as expected. "
            f"Expected: {initial_quantity + 1}, Got: {updated_quantity}."
        )

        # Remove the item from the cart
        home_page.remove_from_cart(item_to_test)
        logger.info(f"Item {item_to_test} removed from the cart in cycle {cycle}.")

        # Verify cart count resets to initial value
        updated_quantity = home_page.get_cart_quantity()
        assert updated_quantity == initial_quantity, (
            f"Cycle {cycle}: Cart quantity did not reset to the initial value. "
            f"Expected: {initial_quantity}, Got: {updated_quantity}."
        )

    logger.info(f"Test passed: Add and remove the same item {cycles} times successfully.")


@pytest.mark.order(6)
def test_cart_count_persistence_after_app_minimize(driver, timeout=2):
    """
    Objective: Verify the cart count persists when the app is minimized and reopened.

    Steps:
    1. Perform a valid login using credentials from environment variables.
    2. Verify login was successful.
    3. Add an item to the cart.
    3. Retrieve the initial cart quantity.
    2. Minimize the app and reopen it.
    3. Check if the cart count is retained.

    :param driver: Appium WebDriver instance provided by the pytest fixture.
    :param timeout: Timeout in seconds for keeping the app in the background. By default, set to 2 seconds.
    :raises AssertionError: If the cart count does not persist after app minimize and reopen.
    """

    # Fetch credentials from environment variables
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    # Ensure credentials are set
    assert username is not None, "TEST_USERNAME environment variable is not set."
    assert password is not None, "TEST_PASSWORD environment variable is not set."
    logger.info("Credentials fetched from environment variables.")

    login_page = LoginPage(driver)

    # Step 1: Ensure login page is loaded and perform valid login
    assert login_page.is_on_login_page(), "Login page not loaded: Login form is not displayed."
    login_page.perform_login(username, password)
    logger.info("Login performed successfully.")

    home_page = HomePage(driver)

    # Step 2: Verify login was successful
    assert home_page.is_logged_in(), "Login failed: Unable to access the home page."
    logger.info("Login verified, user is on the home page.")

    # Step 3: Retrieve available items and add the first item to the cart
    items_available = home_page.get_available_items()
    assert items_available, "No items available to add to the cart."
    logger.info(f"Available items retrieved: {len(items_available)} items found.")
    home_page.add_to_cart(items_available[0])
    logger.info(f"Item {items_available[0]} added to the cart.")

    # Step 5: Retrieve the initial cart quantity
    initial_quantity = home_page.get_cart_quantity()
    assert initial_quantity is not None, "Cart quantity could not be retrieved or cart element is not visible."
    logger.info(f"Initial cart quantity retrieved: {initial_quantity}")

    # Step 6: Minimize the app
    driver.background_app(timeout)

    # Step 7: Check if the cart count is retained
    updated_quantity = home_page.get_cart_quantity()
    logger.info(f"Updated cart quantity retrieved: {updated_quantity}")

    # Assertion: Verify the cart count is the same as it was before the app was minimized
    assert updated_quantity == initial_quantity, f"Cart quantity not retained after app minimize: Expected {initial_quantity}, but got {updated_quantity}."
    logger.info(f"Test passed: Cart quantity successfully retained.")