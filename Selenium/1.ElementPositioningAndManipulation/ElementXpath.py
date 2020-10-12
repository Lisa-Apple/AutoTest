# 基于Firefox浏览器 的 xpath元素定位
# 辅助工具 Firebug Firepath
# coding:utf-8
# xpath: xml路径语言

# xpath属性定位
# 1.通过元素id name class这些属性进行定位
# 2.如果元素没有id name class这些属性 可以通过其他元素进行定位
# 3.通过xpath标签定位
# 4.通过父元素定位
# 5.通过索引定位
# 6.元素属性的逻辑运算

# 继续以百度搜索为例：
# 百度搜索框的html:
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# ‘百度一下’按钮的html:
# <input type="submit" id="su" value="百度一下" class="bg s_btn">

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 1.用元素属性定位：
# (1)用xpath通过id属性定位
# element = driver.find_element_by_xpath('//*[@id="kw"]')\
# (2)用xpath通过name属性定位
# element = driver.find_element_by_xpath('//*[@name="wd"]')
# (3)用xpath通过class属性定位
# element = driver.find_element_by_xpath('//*[@class="s_ipt"]')

# 2.用xpath通过其他元素定位 如这里的autocomplete="off"
# element = driver.find_element_by_xpath('//*[@autocomplete="off"]')

# 3.用xpath通过标签定位
# element = driver.find_element_by_xpath('//input[@id="kw"]')

# 4.用xpath通过父元素定位 层级定位
# 百度搜索框的父元素html:
# <span class="bg s_btn_wr"><input type="submit" id="su" value="百度一下" class="bg s_btn"></span>
# element = driver.find_element_by_xpath('//span[@class="bg s_btn_w"]/input')  #报错了 元素名称重复
# 百度搜索框的爷爷html:
# <form id="form" name="f" action="/s" class="fm">
#     ...
#         <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
#     <span class="soutu-btn">
#     ...
#     </span>
#     <span class="bg s_btn_wr">
#         <input type="submit" id="su" value="百度一下" class="bg s_btn">
#     </span>
# </from>
# element = driver.find_element_by_xpath('//form[@name="f"]/span/input')

# 5.用xpath通过索引定位 索引从1开始而不是0
# element = driver.find_element_by_xpath('//form[@name="f"]/span[2]/input')

# 6.用xpath通过属性逻辑定位 and or not
element = driver.find_element_by_xpath('//*[@id="kw" and @class="s_ipt"]')

# 搜索想要的内容
element.send_keys('天官赐福')
driver.find_element_by_xpath('//*[@id="su"]').click()

# 页面等待3秒后 关闭浏览器进程
time.sleep(3)
driver.quit()