from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)

# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('E:\\github_project\\Learn\\软件测试\\Selenium\\upload.txt')

sleep(2)

driver.quit()


# 知识点：文件上传(send_keys())