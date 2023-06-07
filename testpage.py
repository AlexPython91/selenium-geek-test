from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FILED = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FILED = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FILED)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FILED)
        pass_field.clear()
        pass_field.send_keys(word)

    def clic_login_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        error_text = error_field.text
        return error_text

