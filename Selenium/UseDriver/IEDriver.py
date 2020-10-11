__author__ = 'wanglisha'  # 作者

# coding:utf-8             # 建议所有都加编码

# 导入webdriver包
from selenium import webdriver
# import time

#  创建web driver对象 指明使用ie浏览器
driver = webdriver.Ie()

# 访问百度 在百度输入框输入‘selenium’ 点击确定后 查询
driver.get("http://www.baidu.com")
# 一个控件有若干属性id 、name、（也可以用其它方式定位），百度输入框的id 叫kw  在输入框里输入 selenium
driver.find_element_by_id("kw").send_keys("selenium")
# 搜索的按钮的id 叫su 需要点一下按钮click()
driver.find_element_by_id("su").click()

# 把页面title 打印出来    当没看到整个脚本执行过程时，看到打印出这句话，就说明页面被正确打开了
print(driver.title)

# time.sleep(3)
# 退出并关闭窗口的每一个相关的驱动程序 类似的表达为 driver.close()
driver.quit()
# driver.close()     #关闭当前窗口