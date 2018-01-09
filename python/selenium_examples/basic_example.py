from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox()
# binary = FirefoxBinary("/root/Downloads/firefox/firefox-bin")
# driver = webdriver.Firefox(firefox_binary=binary)

driver.get("http://www.devdungeon.com")
driver.save_screenshot("D:\\test.png")

driver.close()

