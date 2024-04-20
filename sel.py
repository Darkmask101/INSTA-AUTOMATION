from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class insta:
    #SAGAR IF YOU ARE READING THIS INSTALL SELENIUM AND CHECK YOUR CHROME VERSION AND DOWNLOAD THE RESPECTIVE WEBDRIVER FOR YOUR CHROME 
    service = Service(executable_path="/home/sourav/Desktop/chromedriver")
    driver = webdriver.Chrome(service=service)

    #LOGIN CREDENTIALS
    USERNAME = 'tapanbiswas2341@gmail.com'
    PASS = 'XjuY#f9,7p;H)8Q'

    def loogin(self, USERNAME, PASS,driver,service):
        driver.get('https://www.instagram.com/accounts/login/')

        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys(USERNAME)

        time.sleep(3)

        pass_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        pass_field.send_keys(PASS)

        time.sleep(2)

        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
        login_button.click()

        time.sleep(15)
        driver.get('https://www.instagram.com/direct/t/17843018411832095')
        time.sleep(20)


    def spam(self,driver,service):
        i = 1
        skip_but = driver.find_element(By.XPATH, 'html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        skip_but.click()
        while i > 6:
           #:
            time.sleep(4)
            text_but.send_keys(Keys.ENTER)
            time.sleep(5)
            text_but = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_Y5"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')))
            text_but.send_keys("hello" + Keys.ENTER)
            i += 1
           #except e as error:
               #print('error')


# create an instance of the insta class
my_insta = insta()
#html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]
# call the loogin method on the instance
my_insta.loogin(my_insta.USERNAME, my_insta.PASS, my_insta.driver, my_insta.service)
time.sleep(15)
my_insta.spam(my_insta.driver, my_insta.service)
time.sleep(3)