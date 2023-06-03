import time

import yaml
from module import Site

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)
site = Site(test_data['address'])


def test_step1(x_selector1, x_selector2, btn_selector, x_selector3, expected_result):
    input_login = site.find_element("xpath", x_selector1)
    input_login.send_keys("test")

    input_psw = site.find_element("xpath", x_selector2)
    input_psw.send_keys("test")

    submit_button = site.find_element("css", btn_selector)
    submit_button.click()

    err_label = site.find_element("xpath", x_selector3)

    assert err_label.text == expected_result


def test_step2(x_selector1, x_selector2, btn_selector, login_verification, user_name):
    input_login = site.find_element("xpath", x_selector1)
    input_login.clear()
    input_login.send_keys(test_data['login'])

    input_psw = site.find_element("xpath", x_selector2)
    input_psw.clear()
    input_psw.send_keys(test_data['password'])

    submit_button = site.find_element("css", btn_selector)
    submit_button.click()

    enter_text = site.find_element("xpath", login_verification)
    assert enter_text.text == user_name


def test_step3(btn_create_post, x_selector4, x_selector5, x_selector6, save_btn_post, x_selector7, check_new_post):
    button_create = site.find_element("xpath", btn_create_post)
    button_create.click()

    input_title = site.find_element("xpath", x_selector4)
    input_title.send_keys(test_data["title_post"])

    input_des = site.find_element("xpath", x_selector5)
    input_des.send_keys(test_data["descr_post"])

    input_content = site.find_element("xpath", x_selector6)
    input_content.send_keys(test_data["content_post"])

    time.sleep(test_data["sleep_time"])
    btn_save = site.find_element("xpath", save_btn_post)
    btn_save.click()
    time.sleep(test_data["sleep_time"])

    check_title = site.find_element("xpath", x_selector7)
    assert check_title.text == check_new_post

    site.close_connect()

