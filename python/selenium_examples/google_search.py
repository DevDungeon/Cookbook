# Searches Google for something
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox()

driver.get("https://www.google.com")

inputs = driver.find_elements_by_tag_name('input')
for i in inputs:
    if i.get_attribute('title') == 'Search':
        i.send_keys('my search query')
        i.send_keys(Keys.RETURN)
        break


