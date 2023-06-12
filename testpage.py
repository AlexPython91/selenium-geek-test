import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import requests


class TestSearchLocators:
    locators_dict = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        locators_dict[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        locators_dict[locator] = (By.CSS_SELECTOR, locators["css"][locator])


with open("testdata.yaml") as f2:
    user_set = yaml.safe_load(f2)


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description is None:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.exception(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked to {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"Fiend text {text} in field {element_name}")
        return text

    # Methods for entering text in fields
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_LOGIN_FIELD"], word,
                                   description="Login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_PASS_FIELD"], word,
                                   description="Password form")

    def input_form_name(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_FORM_NAME_INPUT"], word,
                                   description="Title in form")

    def input_form_email(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_FORM_EMAIL_INPUT"], word,
                                   description="Email in form")

    def input_form_content(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_FORM_CONTENT_INPUT"], word,
                                   description="Content in form")

    def input_title_new_post(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_TITLE_NEW_POST"], word,
                                   description="Title in new post")

    def input_description_new_post(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_DESCRIPTION_NEW_POST"], word,
                                   description="Description in new post")

    def input_content_new_post(self, word):
        self.enter_text_into_field(TestSearchLocators.locators_dict["LOCATOR_CONTENT_NEW_POST"], word,
                                   description="Content in new post")

    # Clicked to button methods
    def click_login_button(self):
        self.click_button(TestSearchLocators.locators_dict["LOCATOR_LOGIN_BTN"], description="Click login button")

    def button_contact(self):
        self.click_button(TestSearchLocators.locators_dict["LOCATOR_CONTACT_BTN"], description="Click contact button")

    def contact_us_btn(self):
        self.click_button(TestSearchLocators.locators_dict["LOCATOR_BTN_CONTACT_US"],
                          description="Click contact us button")

    def new_post_btn(self):
        self.click_button(TestSearchLocators.locators_dict["LOCATOR_NEW_POST_BTN"], description="Click new post button")

    def button_save_new_post(self):
        self.click_button(TestSearchLocators.locators_dict["LOCATOR_BTN_NEW_POST"],
                          description="Click save new post button")

    # Methods for getting text
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.locators_dict["LOCATOR_ERROR_FIELD"],
                                          description="Find error text")

    def check_enter_user(self):
        return self.get_text_from_element(TestSearchLocators.locators_dict["LOCATOR_BTN_HOME"],
                                          description="Checking entering")

    def check_open_form(self):
        return self.get_text_from_element(TestSearchLocators.locators_dict["LOCATOR_TITLE_FORM"],
                                          description="Checking open form")

    def get_alert_text(self):
        alert_text = self.driver.switch_to.alert.text
        logging.info(alert_text)
        return alert_text

    def get_new_post(self):
        return self.get_text_from_element(TestSearchLocators.locators_dict["LOCATOR_TITLE_POST"],
                                          description="Checking open form for create new post")

    def get_not_me_posts(self, token):
        try:
            response = requests.get(user_set['posts'], headers={'X-Auth-Token': token},
                                    params={'owner': 'notMe', 'page': 1})
            listTitle = []
            for i in response.json()['data']:
                listTitle.append(i['title'])
            return listTitle
        except:
            logging.error('Dont get list not me posts')
            return None

    def create_new_post(self, token):
        try:
            response = requests.post(user_set['posts'], headers={'X-Auth-Token': token},
                                     params={'title_post': user_set['title_post'],
                                             'descr_post': user_set['descr_post'],
                                             'content_post': user_set['content_post']})
            return response.json()
        except:
            logging.error('Error. Dont create new post')
            return None

    def get_my_posts(self, token):
        try:
            response = requests.get(user_set['post'], headers={'X-Auth-Token': token})
            listDescription = []
            for i in response.json()['data']:
                listDescription.append(i['description'])
            return listDescription
        except:
            logging.error('Error. Dont get list my posts')
            return None
