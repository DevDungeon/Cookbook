from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("/root/Downloads/firefox/firefox-bin")
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("http://www.devdungeon.com")
driver.save_screenshot("/Users/jleon/test.png")

driver.close()

