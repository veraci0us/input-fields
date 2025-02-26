from selenium.webdriver.common.action_chains import ActionChains
from random import choice

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        self.scroll_to(element)
        return element
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def fill_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def check_checkbox(self, locator, options):
        all_elements = self.find_elements(locator)

        for element in all_elements:
            checkbox_value = element.get_attribute('value') 
            
            if checkbox_value in options and not element.is_selected():
                self.scroll_to(element)
                element.click()

    def select_radio(self, locator):
        radio = self.find_element(locator)
        radio.click()

    def select_option(self, parent_locator, child_locator):
        select = self.find_element(parent_locator)
        select.click()
        options = self.find_elements(child_locator)
        choice(options).click()
        
    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()
        
