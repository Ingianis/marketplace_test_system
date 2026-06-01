from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    # locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        super().open(self.URL)         
        
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_text(self):
        return self.find(self.ERROR).text