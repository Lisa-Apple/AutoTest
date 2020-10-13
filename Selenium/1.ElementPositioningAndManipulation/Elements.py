# 定位一组元素
# find_elements

# 使用：页面有多个元素需要定位 一个个查找太过繁琐
# 案例：百度搜索“测试部落”
# 目标：定位一组元素 随机操作其中任意元素

# coding:utf-8
from selenium import webdriver
from time import sleep
import random

# 打开浏览器并进行搜索“测试部落”
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id('kw').send_keys('测试部落')
driver.find_element_by_id('kw').submit()  #submit是回车操作
driver.maximize_window()

# 定位页面所有的查找信息
# 所有的搜索行元素都前都有 h3.t >a :
# <h3 class="t">
#     <a data-click="{
# 			'F':'778317EA',
# 			'F1':'9D73F1E4',
# 			'F2':'4CA6DDEA',
# 			'F3':'54E5243F',
# 			'T':'1602572269',
# 						'y':'3EF7FB0F'
# 												}" href="https://www.baidu.com/link?url=7EuzJV62QZDGoMq9uNFTra-Xhmajk7MCR36x5VC_XcfRkIuucpKpZHvZ4W_9pbfX&amp;wd=&amp;eqid=e578056900030d74000000045f854fec" target="_blank" class="">testerhorde<em class="">测试部落</em></a></h3>
search_result = driver.find_elements_by_css_selector("h3.t >a")
print(type(search_result))

# 打印所有查找到的url
for i in search_result:
    print(i.get_attribute("href"))

# 如获取到9条 从9条中随机抽取1条
# 随机函数：random
# 设置随机数的范围 random.randint(0,8)
# 设置随机值
temp = random.randint(0,8)
print(temp)

# 随机获取一条href 跳转链接
temp_result = search_result[temp].get_attribute("href")
print(temp_result)
search_result[temp].click()

sleep(3)
driver.quit()