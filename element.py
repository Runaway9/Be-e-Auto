from selenium import webdriver
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class get_element():

    driver = webdriver.Chrome()
    driver.get('https://bees.fswork.cc/#/auth')
    # 窗口最大化
    driver.maximize_window()
    # 账号
    username = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/input')
    username.send_keys('15501411920')
    # 密码
    pwd = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/input')
    pwd.send_keys('Runaway9')
    # 登陆按钮
    login = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/button[2]/span')
    login.click()
    time.sleep(1)
    # 工作管理按钮
    managework = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]/div')
    managework.click()
    time.sleep(1)
    # 个人周报
    weekreport = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]/ul/li[2]')
    weekreport.click()
    time.sleep(2)
    # 第N周
    week = driver.find_element(By.XPATH, "//div[@class='ivu-select-selection']")
    week.click()
    time.sleep(2)
    #
    # try:
    #     week = driver.find_element(By.XPATH, "//div[@class='ivu-select-selection']")
    #     print("找到元素：", week.text)
    # except NoSuchElementException:
    #     print("未找到元素")
    # time.sleep(3)
    # 选择
    xpath = "/html/body/div[11]/ul[2]/li[{index}]"
    select = driver.find_element(By.XPATH, xpath.format(index=1))
    select.click()
    time.sleep(2)
    # 添加工作记录
    addwork = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button[1]")
    addwork.click()
    time.sleep(2)
    # 项目归属
    project = driver.find_element(By.XPATH, "/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div[1]/div/input")
    project.click()
    hengxiang = driver.find_element(By.XPATH, "/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div[2]/ul[2]/li[3]")
    hengxiang.click()
    # 任务类型
    aimtype = driver.find_element(By.XPATH, "/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input")
    aimtype.click()
    xitongceshi = driver.find_element(By.XPATH, "/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div/span/ul/li[5]")
    xitongceshi.click()
    # 分发项目

    # 任务名称
    # 任务编号
    # 任务角色
    # 任务目标
    # 相关人员
    # 任务进度
    # 是否为计划内容
    # 延迟原因
    # 任务描述
    # 任务备注
    # 星期一
    # 星期二
    # 星期三
    # 星期四
    # 星期五
    # 星期六
    # 星期日
    # 保存
    # 提交周报
    # 提交
