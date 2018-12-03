from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

first_url = 'http://www.baidu.com'
print(first_url)
driver.refresh()
driver.get(first_url)

second_url = 'http://news.baidu.com'
print(second_url)
driver.get(second_url)

print(first_url)
driver.back()

print(second_url)
driver.forward()

sleep(2)
driver.quit()