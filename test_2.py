import yaml
from testpage import OperationsHelper
import logging

with open("testdata.yaml") as f:
    user_set = yaml.safe_load(f)


def test_step1(browser, login, check_text):
    logging.info('Start API test 1')
    test_page = OperationsHelper(browser)
    assert check_text in test_page.get_not_me_posts(login)


def test_step2(browser, login, description):
    logging.info('Start API test 2')
    test_page = OperationsHelper(browser)
    test_page.create_new_post(login)
    assert description in test_page.get_my_posts(login)
