from pages.form_fields.form_fields import FormFieldsPage
from utils.test_data import TestData, URL
import allure

class TestFormFields():
    @allure.title('Test Form Fields')
    @allure.description('This test attempts to fill out the form. It will fail if alert with the message doesn`t pop up')
    @allure.link(URL)
    def test_form_fields(self, setup):
        form_fields_page = FormFieldsPage(setup)
        with allure.step('Fill name input'):
            form_fields_page.fill_name_field(TestData.name)
        with allure.step('Fill password input'):
            form_fields_page.fill_password_field(TestData.password)
        with allure.step('Check checkboxes for Milk and Coffee'):
            form_fields_page.fill_favorite_drink_field(TestData.favorite_drink)
        with allure.step('Choose Yellow color as favorite'):
            form_fields_page.fill_favorite_color()
        with allure.step('Select any option for question "Do you like automation?"'):
            form_fields_page.fill_like_automation()
        with allure.step('Fill email with correct format'):
            form_fields_page.fill_email_field(TestData.email)
        with allure.step('Fill message field'):
            form_fields_page.fill_message_field()
        with allure.step('Click submit'):
            form_fields_page.click_submit_button()
        with allure.step('Check if the alert message is correct'):   
            alert_text = form_fields_page.check_alert()
            assert alert_text == TestData.alert_message
        
