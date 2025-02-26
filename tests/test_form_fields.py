from pages.form_fields.form_fields import FormFieldsPage
from utils.test_data import TestData

class TestFormFields():

    def test_form_fields(self, setup):
        form_fields_page = FormFieldsPage(setup)
        form_fields_page.fill_name_field(TestData.name)
        form_fields_page.fill_password_field(TestData.password)
        form_fields_page.fill_favorite_drink_field(TestData.favorite_drink)
        form_fields_page.fill_favorite_color()
        form_fields_page.fill_like_automation()
        form_fields_page.fill_email_field(TestData.email)
        form_fields_page.fill_message_field()
        form_fields_page.click_submit_button()
        
        alert_text = form_fields_page.check_alert()
        assert alert_text == TestData.alert_message
        
