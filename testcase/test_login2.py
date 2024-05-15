from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageobject.login_page import Login_Page
import time
import allure



@allure.feature("Login")
class Test_Login():

    @allure.title("test_login")
    def test_Login_01(self):
        self.driver = webdriver.Chrome()
        login = Login_Page(self.driver).loginpage(username='wgq_user', password='Aa@123456')
        welcome_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Login_Page(self.driver).welcome),
        )

        # 断言登录成功元素是否存在
        assert welcome_element is not None, "登录成功"
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()