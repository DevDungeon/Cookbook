Selenium Notes
==============

.. contents::

Install
-------

Install using ``pip``::

  pip install selenium

For headless display, also include ``pyvirtualdisplay``::

  pip install pyvirtualdisplay

- Chrome Web Driver: https://sites.google.com/a/chromium.org/chromedriver/home
- Firefox Web Driver: https://github.com/mozilla/geckodriver/releases

Put the executable in your PATH or just drop it in the
same folder with script.

Selenium IDE
------------

Selenium IDE is a browser extension that allows you to record
and replay actions.

Useful functions
================

Take a screenshot of a page
---------------------------

``browser.save_screenshot()``

Headless module
---------------

Use ``pyvirtualdisplay`` and just initialize before creating the driver::

  display = Display(visible=0, size=(800, 600))
  display.start()

Extract all links from page
---------------------------

Use ``browser.find_element[s]_by_*()``

Perform a click action
----------------------

ActionChains() class allows click, double click, send keys, etc

Refer to the ActionChains docs: 
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

Or use the click function::

  driver.find_element*().click()

Login
-----

```python
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("username")
password.send_keys("password")
login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
```

Switching windows
-----------------

Switch windows or frames(tabs?)::
	
  driver.switch_to.window("windowName")
  driver.switch_to.frame("frameName")
