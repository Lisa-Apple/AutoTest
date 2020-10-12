# coding:utf-8
# 基于Chrome浏览器 的 xpath元素定位
# Css定位更快 语法更简单

# 1.通过常规属性id class 标签定位
# 2.其他属性
# 3.css标签
# 4.层级
# 5.索引
# 6.逻辑运算
# 7.模糊匹配
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# <input type="submit" id="su" value="百度一下" class="bg s_btn">
# id属性用#表示 #kw
# class属性用.表示 .s_ipt
# 标签无符号 直接 input

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 1.元素属性id class tag定位 # .
# element = driver.find_element_by_css_selector('.s_ipt')

# 2.其他属性
element = driver.find_element_by_css_selector('[name="wd"]')

# 3.css标签
# element = driver.find_element_by_css_selector('input.s_ipt')
# element = driver.find_element_by_css_selector("input[autocomplete='off']")

# 4.css层级关系
# 类比xpath：
# //form[@class='fm']/span/input
# element = driver.find_element_by_css_selector('form.fm>span>input')

# 5.索引 nth-child(1)
# 类比xpath：
# //form[@name="f"]/span[2]/input
# element = driver.find_element_by_css_selector('form#form>span:nth-child(2)>input')

# 6.逻辑运算
element = driver.find_element_by_css_selector('input[id="kw"][name="wd"]')

# 7.模糊匹配
# [abc^="def"] 选择 abc 属性值以 "def" 开头的所有元素
# [abc$="def"] 选择 abc 属性值以 "def" 结尾的所有元素
# [abc*="def"] 选择 abc 属性值中包含子串 "def" 的所有元素

element.send_keys('天官赐福 百无禁忌')
driver.find_element_by_css_selector('#su').click()
time.sleep(3)

driver.quit()
