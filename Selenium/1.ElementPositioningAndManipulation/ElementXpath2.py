# coding:utf-8
# 用xpath进行模糊匹配
# 案例：点击百度页面超链接'hao123'
# <a href="https://www.hao123.com" target="_blank" class="mnav c-font-normal c-color-t">hao123</a>
# 可类比 find_element_by_link()或find_element_by_partial_link()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http:www.baidu.com')

# driver.find_element_by_link_text('hao123').click()
driver.find_element_by_xpath('//*[@id="s-top-left"]/a[2]').click()

time.sleep(3)
driver.quit()