from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from base.basepage import BasePage
class Login_Page(BasePage):

    # 属性

    


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
