from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestFrame:
    def test_frame(self):
        driver = webdriver.Chrome('/home/egor/Tools/chromedriver')
        driver.get('http://the-internet.herokuapp.com/frames')
        driver.find_element(By.CSS_SELECTOR, '[href="/iframe"]').click()
        driver.implicitly_wait(10)
        driver.switch_to.frame(driver.find_element(By.ID, 'mce_0_ifr'))
        a = driver.find_element(By.CSS_SELECTOR, '#tinymce > p')
        assert a.text == "Your content goes here."

        time.sleep(3)
        driver.close()
