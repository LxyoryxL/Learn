# 百度设置弹出的窗口是不能通过前端工具进行定位的，这时候可以通过 switch_to_alert() 方法接受这个弹窗

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至‘设置’链接
link=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)

# 保存设置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()

driver.quit()

# 知识点：警告框处理