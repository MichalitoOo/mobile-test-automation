import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "3d76494a",
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": "com.swaglabsmobileapp.MainActivity",
        "automationName": "UiAutomator2",
        "noReset": True,
    }
    # Start the Appium driver
    driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(desired_caps))

    yield driver

    # End the session
    driver.quit()
