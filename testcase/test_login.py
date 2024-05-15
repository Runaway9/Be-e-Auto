import os
import yaml
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.login_page import Login_Page
import allure

@allure.feature("Login")
class Test_Login():

    @allure.title("test_login_success")
    @pytest.mark.parametrize("test_data", yaml.safe_load(open("../data/login_data.yaml", encoding="utf-8"))["login_success"])
    def test_Login_success(self, test_data):
        username = test_data["username"]
        password = test_data["password"]
        expected_message = test_data["expected_message"]

        self.driver = webdriver.Chrome()
        login = Login_Page(self.driver).loginpage(username=username, password=password)

        # 断言登录结果是否符合预期

        welcome_element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(Login_Page(self.driver).welcome),
        )
            # 如果找到元素，则断言成功
        assert welcome_element is not None, expected_message

        # token = None
        # for cookie in self.driver.get_cookies():
        #     if cookie["login"] == "token":
        #         token = cookie["value"]
        #         break
        # assert token != None, "没有找到token"
        #
        # with open('../data/token.yaml', 'w', encoding='utf-8') as file:
        #     yaml.dump(token, file)
        #
        # print('token获取成功', token)


        self.driver.quit()



    @allure.title("test_login_fail")
    @pytest.mark.parametrize("test_data", yaml.safe_load(open("../data/login_data.yaml", encoding="utf-8"))["login_fail"])
    def test_Login_fail(self, test_data):
        username = test_data["username"]
        password = test_data["password"]
        expected_message = test_data["expected_message"]

        self.driver = webdriver.Chrome()
        login = Login_Page(self.driver).loginpage(username=username, password=password)

        welcome_element = WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element_located(Login_Page(self.driver).welcome),
        )
        # 断言登录结果是否符合预期
        assert welcome_element is True, expected_message
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()
