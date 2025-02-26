from pages.base_page.base_page import BasePage
from pages.form_fields.form_fields_locators import FormFieldsLocators
from utils.find_longest_word import find_longest_word

class FormFieldsPage(BasePage):  
    def fill_name_field(self, text):
        self.fill_text(FormFieldsLocators.name_field, text)

    def fill_password_field(self, text):
        self.fill_text(FormFieldsLocators.password_field, text)

    def fill_favorite_drink_field(self, options):
        self.check_checkbox(FormFieldsLocators.favorite_drink_field, options)

    def fill_favorite_color(self):
        self.select_radio(FormFieldsLocators.favorite_color_field)
        
    def fill_like_automation(self):
        self.select_option(FormFieldsLocators.like_automation_select_field, FormFieldsLocators.like_automation_options_field)

    def fill_email_field(self, email):
        self.fill_text(FormFieldsLocators.email_field, email)

    def fill_message_field(self):
        list_elements = self.find_elements(FormFieldsLocators.automation_tools)
        list_elements_texts = [(element.text, len(element.text.replace(" ", ""))) for element in list_elements]
        longest_word = find_longest_word(list_elements_texts)
        message = f"There are {len(list_elements)} automation tools. The longest one is {longest_word}"
        self.fill_text(FormFieldsLocators.message_field, message)
    
    def click_submit_button(self):
        self.click_button(FormFieldsLocators.submit_button)

    def check_alert(self):
        return self.driver.switch_to.alert.text