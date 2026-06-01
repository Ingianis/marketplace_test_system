from pages.login_page import LoginPage
import pytest

#successful login
def test_successful_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in browser.current_url, "Login failed: inventory page not loaded"

#negative parametrize login with errros
@pytest.mark.negative 
@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "locked out"), ("standard_user", "wrong_password", "do not match"), ("", "secret_sauce", "Username is required"), ("standard_user", "", "Password is required")]) 
def test_login_negative(username, password, expected_error, browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(username, password)
    error_text = login_page.get_error_text()
    assert expected_error in error_text, f"Expected error message '{expected_error}' not found in '{error_text}'"
