class BasePage:
    # 属性-->初始化数据
    def __init__(self, driver):
        self.driver = driver
    # 定位元素方法
    def locator(self, loc):
        return self.driver.find_element(*loc)
    # 输入方法
    def input(self, loc, value):
        locator = self.locator(loc).send_keys(value)
    # 点击方法
    def click(self, loc):
        locator = self.locator(loc).click()
    # 加载项目地址
    def geturl(self, url):
        self.driver.get(url)