import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)
    browser = test_data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def error_text():
    return "401"


# @pytest.fixture()
# def x_selector1():
#     return """//*[@id="login"]/div[1]/label/input"""
#
#
# @pytest.fixture()
# def x_selector2():
#     return """//*[@id="login"]/div[2]/label/input"""
#
#
# @pytest.fixture()
# def btn_selector():
#     return "button"
#
#
# @pytest.fixture()
# def x_selector3():
#     return """//*[@id="app"]/main/div/div/div[2]/h2"""
#
#
# @pytest.fixture()
# def expected_result():
#     return "401"
#
#
# @pytest.fixture()
# def login_verification():
#     return """//*[@id="app"]/main/nav/ul/li[3]/a"""
#
#
# @pytest.fixture()
# def user_name():
#     return "Hello, ivanivanov697"
#
#
# @pytest.fixture()
# def btn_create_post():
#     return """//*[@id="create-btn"]"""
#
#
# @pytest.fixture()
# def x_selector4():
#     return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
#
#
# @pytest.fixture()
# def x_selector5():
#     return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
#
#
# @pytest.fixture()
# def x_selector6():
#     return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
#
#
# @pytest.fixture()
# def save_btn_post():
#     return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
#
#
# @pytest.fixture()
# def x_selector7():
#     return """//*[@id="app"]/main/div/div[1]/h1"""
#
#
# @pytest.fixture()
# def check_new_post():
#     return "New title for test"
