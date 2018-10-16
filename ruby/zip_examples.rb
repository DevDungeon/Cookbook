# Zip file examples in Ruby
# gem install rubyzip
require 'zip'


# Create a zip file and add things to it

# Open a zip file and list the things in it

# Get the bytes of a file inside the zip

# Open a passworded zip


# Zip::File.open('file.zip')

#
#
# # https://www.rubydoc.info/github/rubyzip/rubyzip/Zip/File
# Zip::File.open("A:\\my.zip", Zip::File::CREATE) {
#  |zipfile|
#   zipfile.get_output_stream("new_file.txt") { |f| f.puts "New file contents." }
#   zipfile.mkdir("new_folder")
#
# }
#
# # glob
# #
# #https://www.rubydoc.info/github/rubyzip/rubyzip/Zip/File
# Zip::File.open("A:\\my.zip", Zip::File::CREATE) {
#   |zipfile|
#   puts zipfile.read("new_file.txt")
#   zipfile.remove("new_file.txt")
# }