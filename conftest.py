import pytest
import logging
from appium import webdriver
from appium.options.common import AppiumOptions
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the path to the directory containing conftest.py
file = __file__
path = os.path.dirname(os.path.abspath(file))

# Fixture to set up and tear down the Appium driver
@pytest.fixture(scope="function")
def driver():
    """
    Initializes the Appium driver for automated control.

    Desired Capabilities:
        - platformName: Android
        - platformVersion: 15 (adjust to match your test device/emulator)
        - deviceName: Name/ID of the device or emulator
        - appPackage: Package name of the app under test
        - appActivity: Main activity to launch the app
        - app: Path to the APK file
        - automationName: UiAutomator2 for Android automation
        - noReset: Resets app state between tests

    Returns:
        Appium driver instance.
    """
    # Define desired capabilities for the Appium driver
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "15",
        "deviceName": "emulator-5554",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "app": fr"{path}\apks\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
        "automationName": "UiAutomator2",
        "noReset": False,
    }

    # Initialize the Appium driver
    driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(desired_caps))

    yield driver  # Provide the driver to the test function

    # Quit the driver session after the test
    driver.quit()


# Pytest hook to handle additional logic for test reports
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test reports and handle failures.
    Logs the outcome of each test and captures a screenshot on test failure.

    Args:
        item: The test item object (test function).
        call: The stage of the test (setup/call/teardown).
    """
    # Capture the outcome of the test
    outcome = yield
    report = outcome.get_result()

    # Initialize a logger for debugging purposes
    logger = logging.getLogger("test_logger")
    logger.info(f"Test {item.name} finished with outcome: {report.outcome}")

    if report.outcome == "failed":
        logger.error(f"Test failed at {item.name} with {report.longrepr}")

    # Capture a screenshot if the test fails during the 'call' phase (during test function execution)
    if call.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # Access driver from test function args
        if driver:
            # Save the screenshot to a specified path
            screenshot_path = f"debug/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            pytest.fail(f"Test failed. Screenshot saved to {screenshot_path}", pytrace=False)
