from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    # locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def open(self):
        super().open(self.URL)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    def get_confirmation_text(self):
        return self.find(self.CONFIRMATION).text