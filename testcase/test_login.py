import pytest
from selenium import webdriver
from pageobject.login_page import Login_Page
import time
import allure


@allure.feature("Login")
class Test_Login():

    @allure.title("test_login")
    def test_login(self):
        self.driver = webdriver.Chrome()
        login = Login_Page(self.driver).loginpage(username='15501411920', password='Runaway9')
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py', '--alluredir', './result'])