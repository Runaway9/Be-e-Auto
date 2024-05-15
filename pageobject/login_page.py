from telnetlib import EC

from selenium.webdriver.common.by import By
from base.basepage import BasePage
class Login_Page(BasePage):

    # 属性
    username = (By.ID, 'userAcountàuacount')
    password = (By.ID, 'pwàp')
    login_btn = (By.XPATH, '//*[@id="loginform"]/button')
    welcome = (By.XPATH, '//*[@id="header"]/div[2]/div/div/div')
    url = 'http://192.168.0.154:8240/WGQYYXT/login.do'

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
