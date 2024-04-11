from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import openpyxl
from selenium.webdriver.common.by import By


#点后端数据分离
excel = openpyxl.load_workbook('D:/AutoTest/bee/beedata.xlsx')
sheet = excel.get_sheet_by_name('beedata')

wd = webdriver.Chrome()
wd.get('https://bees.fswork.cc/#/auth')
#窗口最大化
wd.maximize_window()
#账号
username = wd.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/input')
username.send_keys('15501411920')
time.sleep(3)
#密码
password = wd.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/input')
password.send_keys('Runaway9')
#登陆按钮
login = wd.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/button[2]/span')
login.click()

time.sleep(1)
#工作管理按钮
managework = wd.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]/div')
managework.click()
time.sleep(1)
#个人周报按钮
weekreport = wd.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[1]/ul/li[2]/ul/li[2]')
weekreport.click()
time.sleep(1)
#上周
# Element = wd.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/button/i')
# Element.click()
# time.sleep(1)
# Element.click()
# time.sleep(1)
#增加工作记录按钮
addwork = wd.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button[1]/span')
addwork.click()
time.sleep(2)
#归属项目
projectown = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div[1]/div/input')
projectown.click()
time.sleep(1)
projectselect = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/div[2]/ul[2]/li[3]')
projectselect.click()
#项目任务
aim = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input')
aim.click()
time.sleep(1)
aimselect1 = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div/span/ul/li[5]')
aimselect1.click()
time.sleep(1)
aimselect2 = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div/span/span/ul/li[1]')
aimselect2.click()
#分发项目
place = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div[1]/div/input')
place.click()
time.sleep(1)
placeselect1 = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div[2]/ul[2]/li[3]')
placeselect1.click()
time.sleep(1)
placeselect2 = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div[1]/div/i')
placeselect2.click()
time.sleep(1)
#任务名称
aimname = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[1]/div/div/div/input')
aimname.send_keys(sheet['A2'].value)
time.sleep(1)


#任务角色
aimrole = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[3]/div/div/div/div[1]/div/i')
aimrole.click()
time.sleep(1)
aimroleselect = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[3]/div/div/div/div[2]/ul[2]/li[2]')
aimroleselect.click()
time.sleep(1)
#任务目标
aim3 = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[4]/div/div/div/input')
aim3.send_keys(sheet['B2'].value)
time.sleep(1)
#相关人员
person = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[5]/div/div/div/input')
person.send_keys(sheet['C2'].value)
#任务进度
schedule = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[6]/div/div/div/div[2]/input')
schedule.click()
schedule.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
schedule.send_keys(sheet['D2'].value)
time.sleep(1)
#是否为计划内容
isplane = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[7]/div/div/div/div[1]/div/i')
isplane.click()
time.sleep(1)
isplane1 = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[7]/div/div/div/div[2]/ul[2]/li[1]')
isplane1.click()
#任务描述
describe = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[4]/div[9]/div/div/div/textarea')
describe.send_keys(sheet['E2'].value)
#星期一
Monday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[1]/div/div/div/div[2]/input')
Monday.click()
Monday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Monday.send_keys(sheet['F2'].value)
time.sleep(1)
#星期二
Tuesday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[2]/div/div/div/div[2]/input')
Tuesday.click()
Tuesday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Tuesday.send_keys(sheet['G2'].value)
time.sleep(1)
#星期三
Wednesday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[3]/div/div/div/div[2]/input')
Wednesday.click()
Wednesday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Wednesday.send_keys(sheet['H2'].value)
time.sleep(1)
#星期四
Thursday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[4]/div/div/div/div[2]/input')
Thursday.click()
Thursday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Thursday.send_keys(sheet['I2'].value)
time.sleep(1)
#星期五
Friday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[5]/div/div/div/div[2]/input')
Friday.click()
Friday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Friday.send_keys(sheet['J2'].value)
time.sleep(1)
#星期六
Saturday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[6]/div/div/div/div[2]/input')
Saturday.click()
Saturday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Saturday.send_keys(sheet['K2'].value)
time.sleep(1)
#星期日
Sunday = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[1]/form/div[10]/div[7]/div/div/div/div[2]/input')
Sunday.click()
Sunday.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
Sunday.send_keys(sheet['L2'].value)
time.sleep(1)
#保存
save = wd.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div[2]/div[2]/button[1]')
save.click()
time.sleep(1)
#退出浏览器
wd.quit()