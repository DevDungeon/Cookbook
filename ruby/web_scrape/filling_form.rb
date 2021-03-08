require 'mechanize'

mechanize = Mechanize.new

page = mechanize.get('http://www.devdungeon.com/contact')

form = page.forms.first

form['name'] = 'Test Name'
form['email'] = 'test@example.com'
form['subject'] = 'Test Subject'
form['message'] = 'Test Message'

page = form.submit

puts page.inspect