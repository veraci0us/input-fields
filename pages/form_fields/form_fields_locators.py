from selenium.webdriver.common.by import By

class FormFieldsLocators():
    name_field = (By.ID, 'name-input')
    password_field = (By.XPATH, '//*[@id="feedbackForm"]/label[2]/input')
    favorite_drink_field = (By.NAME, 'fav_drink')
    favorite_color_field = (By.CSS_SELECTOR, '#color3')
    like_automation_select_field = (By.XPATH, '//*[@id="automation"]')
    like_automation_options_field = (By.XPATH, './/option')
    email_field = (By.XPATH, '//input[@id="email"]')
    automation_tools = (By.XPATH, '//*[@id="feedbackForm"]/ul/li')
    message_field = (By.ID, 'message')
    submit_button = (By.ID, 'submit-btn')