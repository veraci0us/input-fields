import pytest
from selenium import webdriver
from utils.test_data import URL

@pytest.fixture
def setup():
    driver = webdriver.Chrome() 
    driver.get(URL)
    driver.maximize_window() 
    yield driver
    driver.quit() 