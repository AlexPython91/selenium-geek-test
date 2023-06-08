from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_BTN_HOME = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_TITLE_FORM = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_FORM_NAME_INPUT = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_FORM_EMAIL_INPUT = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_FORM_CONTENT_INPUT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_BTN_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Sent {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Sent {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Clicked on button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        error_text = error_field.text
        logging.info(f"Find text: {error_text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return error_text

    def check_enter_user(self):
        open_page = self.find_element(TestSearchLocators.LOCATOR_BTN_HOME)
        name_user = open_page.text
        return name_user

    def button_contact(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def check_open_form(self):
        open_form = self.find_element(TestSearchLocators.LOCATOR_TITLE_FORM)
        form_text = open_form.text
        return form_text

    def input_form_name(self, text):
        input_login = self.find_element(TestSearchLocators.LOCATOR_FORM_NAME_INPUT)
        input_login.send_keys(text)

    def input_form_email(self, text):
        input_login = self.find_element(TestSearchLocators.LOCATOR_FORM_EMAIL_INPUT)
        input_login.send_keys(text)

    def input_form_content(self, text):
        input_login = self.find_element(TestSearchLocators.LOCATOR_FORM_CONTENT_INPUT)
        input_login.send_keys(text)

    def contact_us_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT_US).click()

    def check_alert_text(self):
        try:
            alert_text = self.driver.switch_to.alert.text
            return alert_text
        except:
            return None

