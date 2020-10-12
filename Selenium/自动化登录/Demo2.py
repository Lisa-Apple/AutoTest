# coding:utf=8
# 自动化登录gethub代码仓库

# 目标：
# 1.让代码跑起来
# 2.在代码跑起来的基础上 优化代码可读性

# 优化
# 1.如果我想换个账号登录，这时候还得找到登录的账号和密码位置，比较费时。
# 2.我们可以把登录和退出写出两个函数，这样看起来更舒服一点。
# 3.把登录的账号和密码参数化

# coding:utf-8
from selenium import webdriver
import time


def SignIn(driver, username, password):
    # 定位到元素 username or email address 并输入用户名 Lisa-Apple
    driver.find_element_by_id('login_field').send_keys(username)
    # 定位到元素password 并输入密码
    driver.find_element_by_id('password').send_keys(password)
    # 定位到Sign in按钮 点击后进行登录
    driver.find_element_by_name('commit').click()

def CheckUser(driver, username):
    # 登录成功后点击页面右上角的头像 下拉信息中有登录的用户名称
    driver.find_element_by_css_selector('body header div:nth-child(7) details summary').click()
    name = driver.find_element_by_css_selector('strong').text

    # 对比是否是登录的用户名
    if name == username:
        print("登录成功！")
    else:
        print("登录失败！")

def SignOut(driver):
    driver.find_element_by_css_selector('button[type="submit"][class="dropdown-item dropdown-signout"]').click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://github.com/login')
    driver.implicitly_wait(10)

    SignIn(driver, 'Lisa-Apple', 'wanglisha')

    CheckUser(driver, "Lisa-Apple")

    SignOut(driver)

    driver.quit()