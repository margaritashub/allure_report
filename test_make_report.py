import random
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True

def test_guest_can_register(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    rand_number = random.randint(1000000000, 10000000000)
    email = f"user_{str(time.time())}_{rand_number}@ran.dom"
    password = f"pw{rand_number}"
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()
    browser.find_element(By.ID, "id_registration-email").send_keys(email)
    browser.find_element(By.ID, "id_registration-password1").send_keys(password)
    browser.find_element(By.ID, "id_registration-password2").send_keys(password)
    browser.find_element(By.NAME, "registration_submit").click()

    expected_thanks_message = 'Thanks for registering!'
    thanks_message = browser.find_element_by_css_selector('.alert-success .alertinner')
    assert thanks_message.is_displayed(), 'Successful registration message should be visible'
    assert thanks_message.text == expected_thanks_message, \
        f"Successful registration message should be equal fo `{expected_thanks_message}`, but got `{thanks_message.text}` instead"