import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()        # open Chrome
    driver.implicitly_wait(5)          # wait for 5 seconds for elements to appear
    driver.maximize_window()
    yield driver                       # give the driver to the test
    driver.quit()                      # after the test, close the browser

