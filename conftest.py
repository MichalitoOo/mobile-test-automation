import pytest
import logging
import os
from appium import webdriver
from appium.options.common import AppiumOptions

@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "15",
        "deviceName": "emulator-5554",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "app": r"D:\mobile-test-automation\apks\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
        "automationName": "UiAutomator2",
        "noReset": False,
    }


    # Start the Appium driver
    driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(desired_caps))

    yield driver

    # End the session
    driver.quit()


# Hook to capture screenshots on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    logger = logging.getLogger("test_logger")
    logger.info(f"Test {item.name} finished with outcome: {report.outcome}")

    if report.outcome == "failed":
        logger.error(f"Test failed at {item.name} with {report.longrepr}")
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # Access driver from test function args
        if driver:
            screenshot_path = f"debug/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            pytest.fail(f"Test failed. Screenshot saved to {screenshot_path}", pytrace=False)
