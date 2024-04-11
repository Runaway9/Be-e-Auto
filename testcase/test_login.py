import pytest
from selenium import webdriver
from pageobject.login_page import Login_Page
import time


class Test_Login():

    def test_login(self):
        self.driver = webdriver.Chrome()
        login = Login_Page(self.driver).loginpage(username='15501411920', password='Runaway9')
        time.sleep(10)

