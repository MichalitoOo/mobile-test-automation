# Mobile Test Automation Project

Welcome to the **Mobile Test Automation Project**, a simple approach to automating mobile app testing using Python, Appium, and pytest. This project is designed with straightforward practices like the **Page Object Model (POM)** design pattern and includes parameterized test cases to make the tests flexible and reusable.

---

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Running the Tests](#-running-the-tests)
- [Generating a Report](#-generating-a-report)
- [Contact](#-contact)

---

## 🔍 About the Project

This project demonstrates automated testing of a mobile application, focusing on validating key user flows such as login functionality, cart operations, and general user interactions. 

The objectives of this framework include:
- Providing reusable and scalable test components.
- Maintaining clean and modular code with detailed documentation.
- Supporting robust error handling and reporting.

---

## 💻 Technologies Used

- **Python**: Core programming language.
- **Appium**: Mobile app automation framework.
- **Pytest**: Testing framework for managing and executing test cases.
- **Selenium**: WebDriver for locating elements and interacting with the application.
- **Android Emulator** or **Real Device**: Device used for running the tests.

---

## 📂 Project Structure

```plaintext
mobile-test-automation/
├── Pages/
│   ├── base_page.py            # Base class for all pages (contains reusable methods)
│   ├── home_page.py            # Page object for the Home screen
│   ├── login_page.py           # Page object for the Login screen
├── Tests/
│   ├── test_login.py           # Test cases for login functionality
│   ├── test_cart_operations.py # Test cases for cart-related operations
├── conftest.py                 # Pytest fixtures (e.g., driver setup and teardown)
├── requirements.txt            # List of dependencies for the project
├── README.md                   # Project documentation
```


### Prerequisites
1. **Python**: Ensure Python 3.7+ is installed.
2. **Appium Server**: Install Appium (e.g., via `npm install -g appium`).
3. **Android Studio**: Set up the Android SDK and ensure a working emulator or connect a real device.
4. **Java**: Ensure the JDK is installed and configured.

## 🧪 Running the Tests

Follow these steps to execute the test suite:

### Pre-Execution Checklist
1. **Appium Server**: Ensure the Appium server is running.
   ```bash
   appium
   ```
2. **Device/Emulator**: DConfirm that an Android device or emulator is connected and detected:
   ```bash
   adb devices
   ```
   
### To run all tests in the project:
```bash
pytest Tests/
```

### To run a specific test module:
```bash
pytest Tests/test_cart_operations.py
```

### To run a specific test function:
```bash
pytest -k test_add_to_cart
```

## 📊 Generating a Report

To generate an HTML report of the test results, use the `--html` flag:

```bash
pytest --html=report.html
```
After execution, open report.html in a browser to view the detailed test results.

## 📧 Contact

For inquiries, reach out to:

- **Email**: [m.nalevanko13@gmail..com](mailto:m.nalevanko13@gmail.com)  
- **GitHub**: [MichalitoOo](https://github.com/MichalitoOo)
