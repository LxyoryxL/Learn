from selenium import webdriver

dr=webdriver.Chrome()

# 访问百度首页
dr.get('https://www.baidu.com')
print("now access %s" %('https://www.baidu.com'))
# 访问新闻页面
dr.get('https://news.baidu.com')
print("now access %s" %('https://news.baaidu.com'))
#返回（后退）到百度首页
print("back to  %s "%('https://www.baidu.com'))
dr.back()

# 通过id定位输入框:
dr.find_element_by_id("kw")
# 通过link text定位:
dr.find_element_by_link_text("新闻")
# 参数数字为像素点,"设置浏览器宽480、高800显示","然后设置为全屏"：
dr.set_window_size(480, 800)
dr.maximize_window()



driver.quit()










# 章节：selenium 元素定位、控制浏览器操作