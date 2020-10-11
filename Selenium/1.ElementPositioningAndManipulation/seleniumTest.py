# coding:utf-8             # 建议所有都加编码
# 页面等待 sleep()
# 页面刷新 driver.refresh()
# 前进和后退 driver.back() driver.forward()
# 修改浏览器窗口大小 driver.set_windows_size(with, height)
# 浏览器截屏 driver.save_screenshot('路径名 + 文件名 + 后缀')
# 退出浏览器进程 driver.quit()
# 关闭浏览器窗口 driver.close()

# 导入webdriver包
from selenium import webdriver
import time

#  创建web driver对象 指明使用Chrome浏览器
driver = webdriver.Chrome()

# 访问百度 在百度输入框输入‘selenium’ 点击确定后 查询
driver.get("http://www.baidu.com")
# 一个控件有若干属性id 、name、（也可以用其它方式定位），百度输入框的id 叫kw  在输入框里输入 selenium
driver.find_element_by_id('kw').send_keys('春眠不觉晓')
# 搜索的按钮的id 叫su 需要点一下按钮click()
driver.find_element_by_id('su').click()
# 把页面title 打印出来    当没看到整个脚本执行过程时，看到打印出这句话，就说明页面被正确打开了
print(driver.title)

# 设置休眠 sleep中可以添加小数和整数
time.sleep(3)
# 等待3秒后刷新页面
driver.refresh()   # 此时显示的是‘春眠不觉晓’页面
time.sleep(3)

# 浏览器后退
driver.back()  # 此时显示的是百度搜索页面
time.sleep(3)
# 浏览器前进
driver.forward()  # 此时显示的是'春眠不觉晓'页面
time.sleep(3)

# 设置浏览器窗口大小
driver.set_window_size(540, 960)
time.sleep(3)
# 设置浏览器窗口为最大
driver.maximize_window()
time.sleep(3)

# 浏览器截屏
# 定保存路径 + 文件名称 + 后缀
driver.save_screenshot('D:\\wanglisha\\Pictures\\Demo2.jpg')

# 退出浏览器进程
driver.quit()

# 关闭浏览器窗口
# driver.close()