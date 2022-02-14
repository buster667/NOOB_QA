from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestCheckBox:
    def test_checkbox(self):
        driver = webdriver.Chrome('/home/egor/Tools/chromedriver')
        driver.get('http://the-internet.herokuapp.com/dynamic_controls')
        driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        driver.find_element(By.CSS_SELECTOR, '[type="button"]').click()
        driver.implicitly_wait(10)
        a = driver.find_element(By.ID, 'message')
        assert a.text == "It's gone!"
        time.sleep(4)


class TestFindInput:
    def test_input_disable(self):
        enable = True
        driver = webdriver.Chrome('/home/egor/Tools/chromedriver')
        driver.get('http://the-internet.herokuapp.com/dynamic_controls')
        searching_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        assert searching_field.is_enabled() != enable
        time.sleep(4)

    def test_input_enable(self):
        driver = webdriver.Chrome('/home/egor/Tools/chromedriver')
        driver.get('http://the-internet.herokuapp.com/dynamic_controls')
        driver.find_element(By.CSS_SELECTOR, '#input-example > button').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "message")))
        driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('Test')
        message_search = driver.find_element(By.ID, "message")
        assert message_search.text == "It's enabled!"
        time.sleep(2)
        driver.close()
