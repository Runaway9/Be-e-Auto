from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/')


time.sleep(2)

login = driver.find_element(By.CLASS_NAME, 'header-login-entry')
login.click()



driver.quit()


