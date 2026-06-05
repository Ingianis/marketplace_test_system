# Autotests Framework for Marketplace

UI and API autotests in Python: UI for saucedemo.com using Page Object,
API for restful-booker. Reports — Allure.

## Stack
Python 3, Pytest, Selenium, requests, Allure, Page Object.

## Installation
```bash
bashpython3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Launch
All tests: pytest -v
Smoke only: pytest -m smoke
API only: pytest tests/api
With Allure report: pytest --alluredir=allure-results then allure serve allure-results

## Structure
pages/ — Page Object: page classes with locators and actions (BasePage is the common parent class)
tests/ — UI and API tests
conftest.py — common fixtures (browser) and a screenshot-on-failure hook
pytest.ini — smoke / regression / negative markers

## Covered
UI: positive and negative login (parametrize), catalog, cart, placing an order
API: CRUD for bookings with token authorization, positive and negative scenarios

## Manual Test Cases
### TC-01: Successful login
Precondition: saucedemo.com is open
Steps:
Enter standard_user in the username field
Enter secret_sauce in the password field
Click the "Login" button
Expected result: the user is redirected to the products catalog (URL contains inventory.html)


### TC-02: Login with a locked-out user
Precondition: the login page is open
Steps:
Enter locked_out_user / secret_sauce
Click "Login"
Expected result: an error message "Sorry, this user has been locked out" is shown; login is not performed

### TC-03: Login with an empty password
Precondition: the login page is open
Steps:
Enter standard_user in the username field
Leave the password field empty
Click "Login"
Expected result: an error message "Password is required" is shown

### TC-04: Add a product to the cart
Precondition: the user is logged in and on the catalog page
Steps:
Click "Add to cart" on a product
Look at the cart icon
Expected result: the cart badge shows "1"; the product is added to the cart

### TC-05: Place an order (full checkout)
Precondition: the user is logged in and has a product in the cart
Steps:
Open the cart
Click "Checkout"
Fill in First Name, Last Name, and Zip/Postal Code
Click "Continue"
Click "Finish"
Expected result: the confirmation message "Thank you for your order!" is displayed

## Checklist
Login: valid credentials / invalid password / non-existent user / empty fields / locked-out user
Catalog: all 6 products displayed, product sorting works
Cart: add product, remove product, cart counter updates correctly
Checkout: field validation, successful order placement, confirmation message