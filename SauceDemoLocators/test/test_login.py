import pickle
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time


@pytest.fixture(autouse=True)
def my_logger():
    logfile = "test.log"
    log = logging.getLogger("my_log")
    log.setLevel(logging.INFO)
    FH = logging.FileHandler(logfile)
    basic_formater = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
    FH.setFormatter(basic_formater)
    log.addHandler(FH)
    return log


@pytest.fixture(autouse=True)
def registration():
    """фикстура для регистрации"""
    driver = webdriver.Chrome('//home/egor/pythonProject/SauceDemoLocators/resourses/chromedriver')
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(8)
    driver.maximize_window()

    driver.find_element(By.ID, 'user-name').send_keys('performance_glitch_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    time.sleep(5)
    driver.find_element(By.ID, 'login-button').submit()

    driver.get('https://www.saucedemo.com/inventory.html')
    pickle.dump(driver.get_cookies(), open('cookies.pkl', 'wb'))
    yield driver
    driver.close()


def test_registration(registration):
    """тест регистрации"""
    driver = registration
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
        title = driver.title
        assert title == "Swag Labs"


def test_find_elements_on_this_page(registration, my_logger):
    """Здесь ищу все элементы на данной странице"""
    driver = registration
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
        elements_bi_id = driver.find_elements(By.XPATH, '//*[@id]')
        for element in elements_bi_id:
            my_logger.info(f'Нашлись элементы по ID. '
                           f'Тэг "{element.tag_name}" имеет ID: "{element.get_attribute("id")}"')

        elements_by_name = driver.find_elements(By.XPATH, '//*[@name]')
        for element in elements_by_name:
            my_logger.info(f'Нашлись элементы по NAME. '
                           f'Тэг "{element.tag_name}" имеет NAME: "{element.get_attribute("name")}"')

        elements_by_class = driver.find_elements(By.XPATH, '//*[@class]')
        for element in elements_by_class:
            my_logger.info(f'Нашлись элементы по CLASS NAME. '
                           f'Тэг "{element.tag_name}" имеет ID: "{element.get_attribute("class")}"')


def test_show_items(registration, my_logger):
    """some info"""
    driver = registration
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    list_of_items = []
    for item in items:
        list_of_items.append(item.text)

    prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    list_of_prices = []
    for price in prices:
        list_of_prices.append(price.text)

    full_information = dict(zip(list_of_items, list_of_prices))
    assert full_information == {'Sauce Labs Backpack': '$29.99', 'Sauce Labs Bike Light': '$9.99',
                                'Sauce Labs Bolt T-Shirt': '$15.99', 'Sauce Labs Fleece Jacket': '$49.99',
                                'Sauce Labs Onesie': '$7.99', 'Test.allTheThings() T-Shirt (Red)': '$15.99'}

    for a, b in full_information.items():
        my_logger.info(f'Этот продукт: "{a} стоит {b}"')

    time.sleep(7)

