from testpage import OperationsHelper
import logging
import time


def test_step1(browser, error_text):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == error_text


def test_step2(browser, check_enter):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("ivanivanov697")
    testpage.enter_pass("bb5e16295e")
    testpage.click_login_button()
    assert testpage.check_enter_user() == check_enter


def test_step3(browser, form_title):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.button_contact()
    time.sleep(3)
    assert testpage.check_open_form() == form_title


def test_step4(browser, alert_text):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.button_contact()
    testpage.input_form_name("Your name")
    testpage.input_form_email("test@email.ru")
    testpage.input_form_content("Enter your content")
    testpage.contact_us_btn()
    time.sleep(3)
    assert testpage.check_alert_text() == alert_text
