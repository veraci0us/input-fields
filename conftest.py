import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome() 
    driver.maximize_window() 
    driver.get('https://practice-automation.com/form-fields/')
    yield driver
    driver.quit() 