from selenium import webdriver
import time


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

time.sleep(3)
driver.get("https://www.baidu.com")

driver.quit()