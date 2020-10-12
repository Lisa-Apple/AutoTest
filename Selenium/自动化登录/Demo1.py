# coding:utf=8
# 自动化登录gethub代码仓库

# 目标：
# 1.让代码跑起来
# 2.在代码跑起来的基础上 优化代码可读性

# 流程整理
# 第一步：打开浏览器
# 第二步：打开github登录页面
# 第三步：设置元素等待implictlywait()
# 第四步：定位元素 输入用户名 密码 点击确定后登录
# 第五步：验证是否登录成功 账户名是否正确
# 第六步：退出登录
# 第七步：退出浏览器进程

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://github.com/login')
driver.implicitly_wait(10)

# 定位到元素 username or email address 并输入用户名 Lisa-Apple
driver.find_element_by_id('login_field').send_keys('Lisa-Apple')
# 定位到元素password 并输入密码
driver.find_element_by_id('password').send_keys('wanglisa')
# 定位到Sign in按钮 点击后进行登录
driver.find_element_by_name('commit').click()

# 登录成功后点击页面右上角的头像 下拉信息中有登录的用户名称
# driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary').click()
# name = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a/strong').text
driver.find_element_by_css_selector('body header div:nth-child(7) details summary').click()
name = driver.find_element_by_css_selector('strong').text

# 对比是否是登录的用户名
if name == "Lisa-Apple":
    print("登录成功！")
else:
    print("登录失败！")

# 页面停留3秒
time.sleep(3)

# 定位元素 Sign out 退出登录
# <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/&quot;,&quot;target&quot;:&quot;SIGN_OUT&quot;,&quot;originating_url&quot;:&quot;https://github.com/&quot;,&quot;user_id&quot;:59208550}}" data-hydro-click-hmac="690d9f51ca4c98ec1d59a1d2ca2b01184b79e9d57096259e137bae5ee80a7175" role="menuitem">
#         Sign out
#       </button>
driver.find_element_by_css_selector('button[type="submit"][class="dropdown-item dropdown-signout"]').click()

# 页面停留3秒
time.sleep(3)

# 退出浏览器进程
driver.quit()






