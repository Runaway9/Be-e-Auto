from telnetlib import EL
from time import sleep
from tkinter import E
from xml.dom.minidom import Element
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import openpyxl

#点后端数据分离
excel = openpyxl.load_workbook('D:/AutoTest/bee/beedata.xlsx')
sheet = excel.get_sheet_by_name('beedata')

wd = webdriver.Chrome()
wd.get('https://bees.sinosoft.ltd/#/auth')
#窗口最大化
wd.maximize_window()
#账号
Element = wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/input')
Element.send_keys('15501411920')
#密码
Element = wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/input')
Element.send_keys('Runaway9')
#登陆按钮
Element = wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/button[2]/span')
Element.click()

time.sleep(1)
#工作管理按钮
Element = wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]/div')
Element.click()
time.sleep(1)
#个人周报按钮
Element = wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]/ul/li[2]')
Element.click()
time.sleep(1)
#上周
# Element = wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/button/i')
# Element.click()
# time.sleep(1)
# Element.click()
# time.sleep(1)
#增加工作记录按钮
Element = wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button[1]/span')
Element.click()
time.sleep(2)
#归属项目
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div[1]/div/input')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div[2]/ul[2]/li[3]')
Element.click()
#项目任务
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div/span/ul/li[5]')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div/span/span/ul/li[1]')
Element.click()
#分发项目
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div[1]/div/input')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div[2]/ul[2]/li[3]')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div[1]/div/i')
Element.click()
time.sleep(1)
#任务名称
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[1]/div/div/div/input')
Element.send_keys(sheet['A2'].value)
time.sleep(1)


#任务角色
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[3]/div/div/div/div[1]/div/i')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[3]/div/div/div/div[2]/ul[2]/li[2]')
Element.click()
time.sleep(1)
#任务目标
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[4]/div/div/div/input')
Element.send_keys(sheet['B2'].value)
time.sleep(1)
#相关人员
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[5]/div/div/div/input')
Element.send_keys(sheet['C2'].value)
#任务进度
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[6]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['D2'].value)
time.sleep(1)
#是否为计划内容
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[7]/div/div/div/div[1]/div/i')
Element.click()
time.sleep(1)
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[7]/div/div/div/div[2]/ul[2]/li[1]')
Element.click()
#任务描述
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[9]/div/div/div/textarea')
Element.send_keys(sheet['E2'].value)
#星期一
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[1]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['F2'].value)
time.sleep(1)
#星期二
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[2]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['G2'].value)
time.sleep(1)
#星期三
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[3]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['H2'].value)
time.sleep(1)
#星期四
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[4]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['I2'].value)
time.sleep(1)
#星期五
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[5]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['J2'].value)
time.sleep(1)
#星期六
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[6]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['K2'].value)
time.sleep(1)
#星期日
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[7]/div/div/div/div[2]/input')
Element.click()
Element.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Element.send_keys(sheet['L2'].value)
time.sleep(1)
#保存
Element = wd.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/div[2]/button[1]')
Element.click()
time.sleep(1)
#退出浏览器
wd.quit()