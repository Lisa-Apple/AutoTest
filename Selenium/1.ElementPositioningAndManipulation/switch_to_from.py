# 主题：switch_to_from 用法详解
# 案例：163邮箱登录 https://mail.163.com/
# 案例html:
# <iframe name="" frameborder="0" id="x-URS-iframe1602581129608.3865" scrolling="no" style="width: 100%; height: 100%; border: none; background: none;" src="https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2020%2F%2Fcss%2F&amp;cf=urs.163.4944934a.css&amp;MGID=1602581129608.3865&amp;wdaId=&amp;pkid=CvViHzl&amp;product=mail163"></iframe>
# frame和iframe
# 功能相同 iframe更加灵活
# frame整个页面的框架
# iframe 内嵌的框架  浮动帧标记


# coding:utf=8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.implicitly_wait(10)
driver.maximize_window()

# 1.切换iframe 用id定位切换
# driver.switch_to_frame('x-URS-iframe1602581129608.3865')
# driver.switch_to.frame('x-URS-iframe1602581129608.3865')  # 输入id或者name
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# 输入邮箱名
driver.find_element_by_name('email').send_keys('wanglisha@163.com')
# 输入登录密码
driver.find_element_by_name('password').send_keys('123456')
# 勾选十天内免登录 checkbox
driver.find_element_by_css_selector('[type="checkbox"]').click()
# 点击登录
driver.find_element_by_xpath('//*[@id="dologin"]').click()

# 退出内嵌的iframe
driver.switch_to.default_content()

sleep(3)
driver.quit()