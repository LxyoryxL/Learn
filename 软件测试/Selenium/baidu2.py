
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text=driver.find_element_by_id('kw')
# 清除文本
search_text.clear()
# 模拟按键输入
search_text.send_keys("selenium")
# 提交表单
search_text.submit()
driver.back()

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)
# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)
# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

# 等待
time.sleep(3)

driver.quit()









# 知识点：WebDriver常用方法