import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure

@pytest.fixture
def logged_in(browser):                 
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(browser)

@pytest.mark.smoke
@allure.feature("Displayed products")
@allure.title("Amount of displayed products on catalog page")
def test_products_displayed(logged_in):
    with allure.step("Check that 6 products are displayed"):
        assert logged_in.items_count() == 6, "Expected 6 products to be displayed"

@allure.feature("Adding to cart")
@allure.title("Cart count after adding product to cart")
@pytest.mark.regression
def test_add_to_cart(logged_in):
    with allure.step("Add backpack to cart"):
        logged_in.add_backpack_to_cart()
    with allure.step("Check if cart count is 1"):
        assert logged_in.cart_count() == "1", "Cart count should be 1 after adding item"

