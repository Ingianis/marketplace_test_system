import pytest
from selenium import webdriver
import allure


@pytest.fixture
def browser():
    driver = webdriver.Chrome()        # open Chrome
    driver.implicitly_wait(5)          # wait for 5 seconds for elements to appear
    driver.maximize_window()
    yield driver                       # give the driver to the test
    driver.quit()                      # after the test, close the browser


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )