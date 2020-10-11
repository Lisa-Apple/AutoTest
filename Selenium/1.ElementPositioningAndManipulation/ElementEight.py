# Obj:八大元素定位
# Auth:Lisa
# Time:2020.10.11 22:12
# coding:utf-8
# webdriver:Chrome

# 1.通过id定位：find_element_by_id()
#
# 2.通过name定位：find_element_by_name()
#
# 3.通过class定位：find_element_by_class_name()
#
# 4.通过tag定位：find_element_by_tag_name()
#
# 5.通过link定位：find_element_by_link_text()
#
# 6.通过partial_link定位：find_element_by_partial_link_text()
#
# 7.通过xpath定位：find_element_by_xpath()
#
# 8.通过css定位：find_element_by_css_selector()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)

# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">

## 使用find_element_by_id()定位元素
element = driver.find_element_by_id('kw')   # 找到百度搜索框元素
element.send_keys('明月曾照江东寒')  # 在百度搜索框中输入文字‘明月曾照江东寒’
driver.find_element_by_id('su').click()  # 点击右侧搜索按钮
time.sleep(3)
# 浏览器回退到百度搜索首页
driver.back()

## 使用find_element_by_name()  / find_element_by_class_name() 定位元素
element = driver.find_element_by_name('wd')   # 报错 说明元素名称不唯一
element = driver.find_element_by_class_name('s_ipt')
element.send_keys('明月曾照江东寒')
driver.find_element_by_id('su').click()  # 点击右侧搜索按钮
time.sleep(3)
# 浏览器回退到百度搜索首页
driver.back()

## 使用find_element_by_tag_name() 定位元素
# element = driver.find_element_by_tag_name('input')  # 运行保存 因为页面中有多个相同tag name的元素 定位失败
# element.send_keys('明月曾照江东寒')
# driver.find_element_by_id('su').click()  # 点击右侧搜索按钮

## 使用 find_element_by_link_text() 定位元素
# 定位百度中‘hao123’超链接
# <a href="https://www.hao123.com" target="_blank" class="mnav c-font-normal c-color-t">hao123</a>
element = driver.find_element_by_link_text('hao123').click()

# 浏览器回退到百度搜索首页
driver.back()

# 使用 find_element_by_partial_link_text() 定位超长超链接元素
element = driver.find_element_by_partial_link_text('ao123').click()

# 浏览器回退到百度搜索首页
driver.back()

# 使用 find_element_by_xpath() 定位元素
# xpath：一种路径语言
# chrome获取元素xpath操作：元素右键copy xpath
element = driver.find_element_by_xpath('//*[@id="kw"]')
element.send_keys('明月曾照江东寒')
driver.find_element_by_id('su').click()  # 点击右侧搜索按钮

# 浏览器回退到百度搜索首页
driver.back()

# 使用 find_element_by_css_selector() 定位元素
element = driver.find_element_by_css_selector('#kw')
element.send_keys('明月曾照江东寒')
driver.find_element_by_id('su').click()  # 点击右侧搜索按钮

# 页面等待3秒
time.sleep(3)
driver.quit()  # 退出浏览器进程