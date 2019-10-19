from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")

# switch_to.frame() 默认可以直接取表单的id 或name属性。
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

driver.quit()



# 知识点：多表单切换（switch_to.frame()）
# 在进入多级表单的情况下，可以通过switch_to.default_content()跳回最外层的页面