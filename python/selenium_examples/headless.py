from selenium import webdriver
from pyvirtualdisplay import Display
 
display = Display(visible=0, size=(800, 600))
display.start()

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("/root/Downloads/firefox/firefox-bin")
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("http://www.devdungeon.com")
driver.save_screenshot("/root/test.png")
driver.close()

display.stop()
