import pytest
from selenium import webdriver
from utils.test_data import URL
import allure

@pytest.fixture
@allure.title('Prereq: Open a link in Chrome')
def setup():
    driver = webdriver.Chrome() 
    driver.get(URL)
    driver.maximize_window() 
    yield driver
    driver.quit() 