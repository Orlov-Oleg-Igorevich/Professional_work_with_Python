import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import config


@pytest.fixture(scope='function')
def browser():
    print('\nStart test')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print('\nEnd test')

def test_enter_yandex(browser):
    link = 'https://passport.yandex.ru/auth/'
    browser.get(link)
    input_email = browser.find_element(By.ID, 'passp-field-login')
    input_email.send_keys(config.EMAIL)
    entr = browser.find_element(By.CSS_SELECTOR, '[data-t="button:action:passp:sign-in"]')
    entr.click()
    input_password = browser.find_element(By.CSS_SELECTOR, '[data-t="field:input-passwd"]')
    input_password.send_keys(config.PASSWORD)
    entr = browser.find_element(By.CSS_SELECTOR, '[data-t="button:action:passp:sign-in"]')
    entr.click()
