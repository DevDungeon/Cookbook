# To run
# 1) Install the Selenium package for Python
#       pip install selenium
# 2) Download the Chrome Web Driver: https://sites.google.com/a/chromium.org/chromedriver/home
# 3) Put the executable in your PATH or just drop it in the same folder with webshotter.py
# 4) Test run with:
#       cat url_list.txt | python webshotter.py
# 5) Verify your screenshots were made (they will be in current working directory)
import sys
import time
from selenium import webdriver

# There are options for Firefox, Edge, and others too
driver = webdriver.Chrome()  # Or specify the binary: webdriver.Chrome(C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")


# For each line provided to STDIN
count = 0
for raw_line in sys.stdin.readlines():
    url = raw_line.strip()
    driver.get(url)
    time.sleep(.5)  # Half a sec to ensure page has time to fully _rendered_ before screenshotting
    driver.save_screenshot(str(count) + ".png")  # Filename is simply an incrementing number
    count += 1

driver.close()
