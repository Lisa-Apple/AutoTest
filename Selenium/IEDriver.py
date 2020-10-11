__author__ = 'wanglisha'  # 作者

# coding:utf-8             # 建议所有都加编码

from selenium import webdriver  # 导入webdriver包

driver = webdriver.Ie()  # 使用ie浏览器
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
####一个控件有若干属性id 、name、（也可以用其它方式定位），百度输入框的id 叫kw  我要在输入框里输入 selenium 。
driver.find_element_by_id("su").click()
####搜索的按钮的id 叫su ，我需要点一下按钮（ click() ）。
print(driver.title)  # 把页面title 打印出来    当没看到整个脚本执行过程时，看到打印出这句话，就说明页面被正确打开了
driver.quit()  # 退出并关闭窗口的每一个相关的驱动程序 类似的表弟为 driver.close()
# driver.close()     #关闭当前窗口