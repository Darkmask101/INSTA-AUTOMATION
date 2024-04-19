from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#SAGAR IF YOU ARE READING THIS INSTALL SELENIUM AND CHECK YOUR CHROME VERSION AND DOWNLOAD THE RESPECTIVE WEBDRIVER FOR YOUR CHROME 
service = Service(executable_path="/home/sourav/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)

#LOGIN CREDENTIALS
USERNAME = 'tapanbiswas2341@gmail.com'
PASS = 'XjuY#f9,7p;H)8Q'


driver.get('https://www.instagram.com/accounts/login/')

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

username_field.send_keys(USERNAME)

time.sleep(3)

pass_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
pass_field.send_keys(PASS)

time.sleep(2)

login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
time.sleep(1)
login_button.click()

time.sleep(30)


time.sleep(15)

driver.get('https://www.instagram.com/agastya_shah.01/')
time.sleep(9)