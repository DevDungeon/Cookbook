require 'nokogiri'
require 'open-uri'

doc = Nokogiri::HTML(open('http://www.devdungeon.com'))

# Search for nodes by css
doc.css('h2').each do |h2|
	puts h2.content
end

# Search for nodes by xpath
doc.xpath('//ul/li').each do |li|
	puts li.content
end

# Or mix and match.
doc.search('h2', '//h4/a').each do |link|
	puts link.content
end

# Print all links
doc.css('a').map { |link|
	puts link.attribute('href') # Link
	puts link.content # Label
}