from selenium.webdriver.common.by import By
from base.basepage import BasePage
class Login_Page(BasePage):

    # 属性
    username = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/input')
    password = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/input')
    login_btn = (By.XPATH, '/html/body/div[1]/div[1]/div[4]/button[2]/span')
    url = 'https://bees.fswork.cc/#/auth'

    # 方法
    def loginpage(self, username, password):
        # 打开网址
        self.geturl(self.url)
        # 输入用户名
        self.input(loc=self.username, value=username)
        # 输入密码
        self.input(loc=self.password, value=password)
        # 点击登陆
        self.click(loc=self.login_btn)
