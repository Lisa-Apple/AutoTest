# 主题：Alert comfirm prompt
# 案例：Alert.html

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = "file:///D:/wanglisha/git/AutoTestLearning/Selenium/1.ElementPositioningAndManipulation/alertDemo.html"
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

# alert
# 1.点击按钮 打开alert
driver.find_element_by_id('alert').click()
# 2.切换到alert
alertObj = driver.switch_to.alert
print(alertObj.text)
sleep(3)
# 3.确认告警框
# alertObj.accept()
# 或点击×
alertObj.dismiss()
sleep(3)

# confirm
# 1.点击按钮 打开comfirm
driver.find_element_by_id('confirm').click()
# 2.切换到comfirm
comfirmObj = driver.switch_to.alert
print(comfirmObj.text)
sleep(3)
# 3.确认
comfirmObj.accept()
sleep(3)

# prompt
driver.find_element_by_id('prompt').click()
promptObj = driver.switch_to.alert
print(promptObj)
sleep(3)
promptObj.send_keys('sorry there is nothing')
promptObj.accept()

sleep(3)
driver.quit()