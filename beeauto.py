from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from element import get_element


get_element.driver.get('https://bees.sinosoft.ltd/#/auth')
get_element.username.send_keys('15501411920')
