require 'selenium-webdriver'

browser = Selenium::WebDriver.for :firefox

# Load a page
begin
  browser.navigate.to 'http://www.devdungeon.com'
rescue
  puts 'Error loading page.'
end


# Get single element by ID
element = browser.find_element(:id, 'node-155')
puts element.text

# Get multiple elements by class
browser.find_elements(:class_name, 'title').each do |e|
  puts e.text
end

# Get element using XPath
element = browser.find_elements(:xpath, "html/body/div[1]")
puts element


# Enter text in search box
element = browser.find_element(:id, 'edit-search-block-form--2')
element.send_keys 'ruby'

# Click the search button
element = browser.find_element(:id, 'edit-submit')
element.click


browser.close