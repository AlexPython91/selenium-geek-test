import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

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


@pytest.fixture()
def error_text():
    return "401"


@pytest.fixture()
def check_enter():
    return f"Hello, {test_data['login']}"


@pytest.fixture()
def get_my_new_post():
    return "New title for test"


@pytest.fixture()
def alert_text():
    return "Form successfully submitted"


@pytest.fixture()
def login():
    response = requests.post(test_data['url'], data={'login': test_data['login'],
                                                     'password': test_data['password']})
    response.encoding = 'utf-8'
    response = response.json()['token']
    return response


@pytest.fixture()
def check_text():
    return 'test'


@pytest.fixture()
def description():
    return 'Post Description'


@pytest.fixture()
def login():
    response = requests.post(test_data['url'], data={'login': test_data['login'],
                                                     'password': test_data['password']})
    response.encoding = 'utf-8'
    return response.json()['token']
