require 'exifr'
files = Dir["*/*"]
# puts files

def print_usage
  puts 'Usage: '
end

# puts ARGV
# puts ARGV.length
#
# if ARGV.length < 2
#   puts 'Not enough arguments. '
#   print_usage
# end
files.each { |path|
  begin
    pic = EXIFR::JPEG.new(path)
    puts path
    if pic.exif? and (pic.gps_latitude or pic.gps_longitude)
      puts path
      puts pic.width.to_s + "x" + pic.height.to_s
      puts "Timestamp " + pic.date_time.to_s
      puts "GPS: " + pic.gps_latitude.to_s + "," + pic.gps_longitude.to_s
      #puts "Model: " + pic.model.to_s
      #puts "Exposure time: " + pic.exposure_time.to_s
      #puts "Fnumber: " + pic.f_number.to_s
    end
    nil
  rescue
# ignored
  end
}