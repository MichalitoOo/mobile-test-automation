from appium import webdriver
import time

from appium.options.common import AppiumOptions

# Define desired capabilities for the device and app
desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",  # Update with your device's version if needed
    "deviceName": "3d76494a",
    "appPackage": "com.swaglabsmobileapp",  # Package name of the app
    "appActivity": "com.swaglabsmobileapp.MainActivity",  # Main activity of the app
    "automationName": "UiAutomator2",  # Essential for Android
}

# Start the Appium driver
driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(desired_caps))

# Wait for the app to load
time.sleep(10)

# Optionally, you can add further interactions with the app here, for example:
# driver.find_element_by_id('some_element_id').click()

# End the session
driver.quit()
