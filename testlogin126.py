from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.126.com')

driver.find_element_by_xpath('//*[@id="auto-id-1541139117282"]').clear()
driver.find_element_by_xpath('//*[@id="auto-id-1541139117282"]').send_keys('username')
driver.find_element_by_id('auto-id-1541139003027').clear()
driver.find_element_by_id('auto-id-1541139003027').send_keys('password')
#driver.find_element_by_css_selector('#auto-id-1555308707751')
driver.find_element_by_id('dologin').click()

driver.quit()