# Given a url in arg 1, pull all images and extract exif

require 'nokogiri'
require 'exifr/jpeg'
require 'open-uri'

puts "Pulling #{ARGV[0]}"
doc = Nokogiri::HTML(open(ARGV[0]))

# Print all links
doc.css('a').map { |link|
    url = "https:" + link.attribute('href')

    File.open('temp.jpeg', "wb") do |file|
        file.write Net::HTTP.get(URI(url))
    end

    image_exif = EXIFR::JPEG.new('temp.jpeg')
    puts image_exif.exif?
    puts image_exif.comment
}

