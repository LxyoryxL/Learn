from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.testclass.net/")

# 获得cookie信息
cookie= driver.get_cookies()
# 向cookie的name 和value中添加会话信息
driver.add_cookie({'name':'lxy','value':'19'}) 
cookie_name=driver.get_cookie('lxy')

# 将获得cookie的信息打印
print(cookie_name)


driver.quit()




# 知识点：cookie操作