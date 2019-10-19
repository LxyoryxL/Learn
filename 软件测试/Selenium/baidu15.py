from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("E:\\github_project\\Learn\\软件测试\\Selenium\\baidu_img.jpg")

driver.quit()


# 知识点：窗口截图（get_screenshot_as_file()）