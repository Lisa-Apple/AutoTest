# (3) 鼠标事件
# 1.鼠标悬停事件
#     1.1 模块：selenium.webdriver.common.action_chains
#     1.2 鼠标悬停：move_to_element()
#     1.3 执行:perfrom()
#     1.4 案例：鼠标悬停百度首页“设置”
#
# 2.右击鼠标
#    contect_click()
# 3.双击鼠标
#    double_click()

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()

# 鼠标悬停
# mouse = driver.find_element_by_link_text("设置")  #有重复元素 错误了
# mouse = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
# ActionChains(driver).move_to_element(mouse).perform()

# 右击鼠标 点击一下， 了解更多
# mouse_right = driver.find_element_by_xpath('//*[@id="lg"]/map/area')
# ActionChains(driver).context_click().perform()

# 双击鼠标
mouse_double = driver.find_element_by_id('kw')
ActionChains(driver).double_click().perform()

sleep(3)
driver.quit()