from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()


									# 显式等待（WebDriverWait类)
									# driver.get("http://www.baidu.com")

									# element = WebDriverWait(driver, 3, 0.5).until_not(
									#                       EC.presence_of_element_located((By.ID, "kw"))
									#                       )
									# element.send_keys('selenium')




# 隐式等待（implicitly_wait()方法）
# 设置隐式等待为10秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
driver.quit()




# 知识点：设置元素等待（WebDriver类提供了两种等待：显式等待、隐式等待）