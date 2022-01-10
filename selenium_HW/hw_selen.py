from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestKinopoisk:

    def test_login(self):
        driver = webdriver.Chrome("/home/egor/Homework/chromedriver/chromedriver")
        driver.get("https://www.kinopoisk.ru/")

        driver.find_element(By.CLASS_NAME, "styles_loginButton__25BMr").click()

        driver.find_element(By.ID, "passp-field-login").send_keys("punckoegor")
        driver.find_element(By.ID, "passp:sign-in").click()
        time.sleep(1)
        driver.find_element(By.ID, "passp-field-passwd").send_keys(")8mLJpHkB-cp9NZ")
        driver.find_element(By.ID, "passp:sign-in").click()
        time.sleep(1)

    def test_successful_login(self):
        driver = webdriver.Chrome("/home/egor/Homework/chromedriver/chromedriver")
        driver.get("https://www.kinopoisk.ru/user/99411663/go/")
        time.sleep(1)

        assert "punckoegor" in driver.page_source
        driver.close()
