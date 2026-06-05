from pages.login_page import LoginPage
import pytest
import allure

#successful login
@allure.feature("Authorisation")
@allure.title("Successful login")
def test_successful_login(browser):
    login_page = LoginPage(browser)
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Enter login and password"):
        login_page.login("standard_user", "secret_sauce")
    with allure.step("Check if catalog page appears"):
        assert "inventory.html" in browser.current_url, "Login failed: inventory page not loaded"

#negative parametrize login with errros
@allure.feature("Authorisation")
@allure.title("Negative login")
@pytest.mark.negative 
@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "locked out"), ("standard_user", "wrong_password", "do not match"), ("", "secret_sauce", "Username is required"), ("standard_user", "", "Password is required")]) 
def test_login_negative(username, password, expected_error, browser):
    login_page = LoginPage(browser)
    with allure.step("Open login page"):
        login_page.open()
    with allure.step(" Mutliple enter with wrong login and password"):   
        login_page.login(username, password)
    with allure.step("Get error"):
        error_text = login_page.get_error_text()
    with allure.step("Check if expected error appears"):
        assert expected_error in error_text, f"Expected error message '{expected_error}' not found in '{error_text}'"
