import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def logged_in(browser):                 
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return CheckoutPage(browser)

@pytest.mark.smoke
def test_checkout_form(logged_in):
    logged_in.open()                   
    logged_in.fill_checkout_form("Sam", "Smith", "12345")
    logged_in.continue_checkout()
    assert "checkout-step-two.html" in logged_in.driver.current_url, "Checkout step two page not loaded"
