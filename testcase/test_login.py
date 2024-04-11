import pytest
from selenium import webdriver
from pageobject.login_page import Login_Page
import time
import allure
import subprocess

@allure.feature("Login")
class Test_Login():

    @allure.title("test_login")
    def test_login(self):
        self.driver = webdriver.Chrome()
        login = Login_Page(self.driver).loginpage(username='15501411920', password='Runaway9')
        time.sleep(10)
        # 运行pytest，并生成allure报告
        subprocess.run(["pytest", "--alluredir=allure-results"])
