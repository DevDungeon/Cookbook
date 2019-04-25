from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.find_element_by_xpath('//input[@title="Search"]').send_keys('my search' + Keys.RETURN)

