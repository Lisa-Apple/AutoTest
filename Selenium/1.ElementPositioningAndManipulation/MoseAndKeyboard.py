# 说明：web界面常用的元素操作办法
# 项目：鼠标和键盘
# 目标：
# (1) 简单操作
# 1.点击鼠标左键 click()
# 2.清空输入框 clear()
# 3.输入字符串 send_keys()
# 4.Enter键提交表单 submit()
# 小输出：浏览器打开“测试部落” 输入搜索关键字 键盘敲击回车
# 网址：https://testerhome.com/
# 元素：<input class="form-control" name="q" type="text" value="" placeholder="搜索本站内容">
# (2) 模拟键盘
# 键盘模块：selenium.webdriver.common.keys
# Enter键：send_keys(Keys.Enter)
# 键盘F1-F12：send_keys(Keys.F1) - send_keys(Keys.F12)
# 复制Ctrl+C: send_keys(Keys.CONTROL,'c')
# 粘贴Ctrl+V：send_keys(Keys.CONTROL,'v')
# 全选Ctrl+A：send_keys(Keys.CONTROL,'a')
# 剪切Ctrl+X：send_keys(Keys.CONTROL,'x')
# 制表符Tab: send_keys(Keys.Tab)
# (3) 鼠标事件
# 1.鼠标悬停事件
# 1.1 模块：selenium.webdriver.common.action_chains
# 1.2 鼠标悬停：move_to_element()
# 1.3 执行:perfrom()
# 1.4 案例：鼠标悬停百度首页“设置” Mouse.py
# 2.右击鼠标
#
# 3.双击鼠标


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://testerhome.com/")
driver.implicitly_wait(10)
# 设置窗口为100%
driver.maximize_window()
element = driver.find_element_by_tag_name("input")
element.clear()
element.send_keys("selenium")
# element.submit()
element.send_keys(Keys.ENTER)

sleep(3)
driver.quit()