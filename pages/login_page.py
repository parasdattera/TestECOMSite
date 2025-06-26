from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, ElementClickInterceptedException
)

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        # Locators
        self.username_input = (By.XPATH, "//input[@id='user-name']")
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def login(self, username, password):
        try:
            self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
            self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        except TimeoutException:
            print("Login elements did not load in time.")
        except NoSuchElementException as e:
            print(f"Element not found during login: {e}")
        except ElementClickInterceptedException:
            print("Login button could not be clicked due to overlay or modal.")
        except Exception as e:
            print(f"Unexpected error during login: {e}")

    def get_error_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text
        except TimeoutException:
            print("Error message not visible in time.")
        except NoSuchElementException:
            print("Error message element not found.")
        return None
