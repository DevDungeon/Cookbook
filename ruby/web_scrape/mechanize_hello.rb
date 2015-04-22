require 'mechanize'

mechanize = Mechanize.new

page = mechanize.get("http://www.devdungeon.com")

puts page.title

page.link_with(text: "Contact").each do |l|
	puts l
end