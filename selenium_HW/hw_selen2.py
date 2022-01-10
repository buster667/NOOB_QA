from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test:

    def test_register(self):
        driver = webdriver.Chrome("/home/egor/Homework/chromedriver/chromedriver")
        driver.get('http://demo.guru99.com/test/newtours/register.php')

        driver.find_element(By.NAME, 'firstName').send_keys('Marty')
        driver.find_element(By.NAME, 'lastName').send_keys('McFly')
        driver.find_element(By.NAME, 'phone').send_keys('+1234567810')
        driver.find_element(By.NAME, 'userName').send_keys('Marty_Mc')
        driver.find_element(By.NAME, 'address1').send_keys('12 Washington Street')
        driver.find_element(By.NAME, 'city').send_keys('Hill Valley')
        driver.find_element(By.NAME, 'state').send_keys('California')
        driver.find_element(By.NAME, 'postalCode').send_keys('12345')
        driver.find_element(By.NAME, 'country').send_keys('USA')
        driver.find_element(By.NAME, 'email').send_keys('Marty12@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('12122323')
        driver.find_element(By.NAME, 'confirmPassword').send_keys('12122323')
        driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)

    def test_check_correct_info(self):
        driver = webdriver.Chrome("/home/egor/Homework/chromedriver/chromedriver")
        driver.get('http://demo.guru99.com/test/newtours/register_sucess.php')
        element_1 = driver.find_element(By.XPATH, '//tr[3]/td/p[1]/font/b')
        try:
            assert element_1.text == 'Dear Marty McFly,'
            print('First name is Marty, last name is McFly')
        except ValueError:
            print('False')
        time.sleep(2)

    def test_username(self):
        driver = webdriver.Chrome("/home/egor/Homework/chromedriver/chromedriver")
        driver.get('http://demo.guru99.com/test/newtours/register_sucess.php')

        element_2 = driver.find_element(By.XPATH, '//tr[3]/td/p[3]/font/b')

        try:
            assert element_2.text == 'Note: Your user name is Marty12@gmail.com.'
            print('User name is Marty12@gmail.com')
        except ValueError:
            print('False')
        time.sleep(2)

