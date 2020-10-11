# 用于打草稿

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_link_text('hao123').click()

time.sleep(3)
driver.quit()
