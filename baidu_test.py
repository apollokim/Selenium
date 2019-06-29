from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))
#element = driver.find_element_by_css_selector('#kw')
element.send_keys('selenium')

'''#获取输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

#返回百度页面底部备案信息
text = driver.find_element_by_id('cp').text
print(text)

#返回元素的属性值，可以是id，name，type或者其他任意属性类型
attribute = driver.find_element_by_id('kw').get_attribute('tpye')
print(attribute)

#返回元素的结果是否可见，返回结果为true或者false
result = driver.find_element_by_id('kw').is_displayed()
print(result)'''

sleep(1)
driver.quit()