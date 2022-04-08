import random
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
)


@pytest.fixture(name='available_user')
def available_test_user():
    test_user = {
        'username': 'test09001',
        'email': 'test0900@gmail.com',
        'password': '12test12'
    }
    yield test_user


@pytest.fixture(name='test_user_credentials')
def generate_new_test_user_credentials():
    random_num = str(random.randint(1, 10000))

    test_user = {
        'username': f'test{random_num}',
        'email': f'selenium_user{random_num}@test.pl',
        'password': f'testregistration{random_num}'
    }
    yield test_user, random_num


def test_homepage_title_present(browser):
    assert "Welcome Quiz player!" in browser.title


def test_user_wrong_credentials_or_not_found(browser):
    browser.find_element(By.LINK_TEXT, "Login").click()
    browser.find_element(By.NAME, "uname").send_keys("no_user")
    browser.find_element(By.NAME, "pass").send_keys("no_pass")
    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.send_keys(Keys.RETURN)
    assert "Wrong credentials (or) User not found" in browser.page_source


def test_redirect_to_correct_register_url(browser):
    browser.find_element(By.LINK_TEXT, "Register").click()
    assert "/register/" in browser.current_url


def test_registration_redirect_without_filled_fields(browser):
    browser.find_element(By.LINK_TEXT, "Register").click()
    WebDriverWait(browser, timeout=3).until(
        lambda driver: driver.find_element(By.NAME, "username")
    ).send_keys("test_user")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    try:
        WebDriverWait(browser, timeout=3).until(
            EC.url_to_be("https://127.0.0.1:8001/login/")
        )
    except TimeoutException:
        assert True


def test_validate_bootstrap_field_validation_message(browser):
    browser.find_element(By.LINK_TEXT, "Register").click()
    email_field = browser.find_element(By.NAME, "email")
    assert "Please fill out this field." in email_field.get_attribute(
        "validationMessage"
    )


def test_register_new_student_user_and_login_logout_as_new_user(browser, test_user_credentials):
    test_user, num = test_user_credentials

    try:
        browser.find_element(By.LINK_TEXT, "Register").click()
        # User name:
        browser.find_element(By.NAME, "username").send_keys(test_user.get('username'))
        # Last_name:
        browser.find_element(By.NAME, "email").send_keys(test_user.get('email'))
        # User_type:
        browser.find_element(By.XPATH, '//*[@id="div_id_usertype"]/div/div[1]/label').click()
        # Password:
        browser.find_element(By.NAME, "password1").send_keys(test_user.get('password'))
        browser.find_element(By.NAME, "password2").send_keys(test_user.get('password'))
        # Submit:

        WebDriverWait(browser, timeout=3).until(
            lambda driver: driver.find_element(By.XPATH, "//button[@type='submit']")
        ).click()

        html = browser.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.END)
    except (
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException,
    ) as err:
        print(str(err))
        assert False
    except Exception as err:
        print("Some error occurred!" + str(err))
        assert False

    assert f"Account created for selenium_user{num}@test.pl!" in browser.page_source
    assert "/login/" in browser.current_url

    browser.find_element(By.NAME, "uname").send_keys(test_user.get('username'))
    browser.find_element(By.NAME, "pass").send_keys(test_user.get('password'))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    assert "Logged In as Student" in browser.page_source
    assert f"Welcome {test_user.get('username')} !" in browser.page_source

    WebDriverWait(browser, timeout=3).until(
        lambda driver: driver.find_element(By.LINK_TEXT, "Logout")
    ).click()

    assert "You are Logged out Successfully." in browser.page_source


def test_user_name_exist_validation(browser, available_user):
    browser.find_element(By.LINK_TEXT, "Register").click()
    # User name:
    browser.find_element(By.NAME, "username").send_keys(available_user.get('username'))
    # Last_name:
    browser.find_element(By.NAME, "email").send_keys(available_user.get('email'))
    # User_type:
    browser.find_element(By.XPATH, '//*[@id="div_id_usertype"]/div/div[1]/label').click()
    # Password:
    browser.find_element(By.NAME, "password1").send_keys(available_user.get('password'))
    browser.find_element(By.NAME, "password2").send_keys(available_user.get('password'))
    # Submit:

    WebDriverWait(browser, timeout=3).until(
        lambda driver: driver.find_element(By.XPATH, "//button[@type='submit']")
    ).click()

    assert '/register/' in browser.current_url
    assert 'A user with that username already exists.' in browser.page_source
