import pytest
from selenium import webdriver

@pytest.fixrure(scope="function")
def browser():
    print("\start browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()