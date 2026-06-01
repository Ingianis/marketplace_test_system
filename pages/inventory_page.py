from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com"

    # locators
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
       
    def items_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEM))

    def add_backpack_to_cart(self):
        self.click(self.ADD_BUTTON)

    def cart_count(self):
        return self.find(self.CART_BADGE).text

    def go_to_cart(self):
        self.click(self.CART)