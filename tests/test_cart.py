import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in(browser):                 
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(browser)

@pytest.mark.smoke
def test_products_displayed(logged_in):  
    assert logged_in.items_count() == 6, "Expected 6 products to be displayed"


@pytest.mark.regression
def test_add_to_cart(logged_in):
    logged_in.add_backpack_to_cart()
    assert logged_in.cart_count() == "1", "Cart count should be 1 after adding item"

