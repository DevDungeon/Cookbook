# Print integer literals
puts 97 # 97 Decimal
puts 077 # 63 Octal
puts 0xFF # 255 Hex
puts 0b00001000 # 8 Binary

# Print integers as string in base 16/10/8/2
puts 255.to_s 16 # ff
puts 255.to_s 10 # 255
puts 255.to_s 8 # 377
puts 255.to_s 2 # 11111111

# ASCII/ord
puts 'a'.ord # 97
puts 'z'.ord # 122
puts 'A'.ord # 65
puts 'Z'.ord # 90
puts '0'.ord # 48
puts '9'.ord # 57

# String as bytes
'some text'.bytes #[255, 255, 255, 255]

# Packing/unpacking raw bytes
# http://ruby-doc.org/core-2.0.0/Array.html#method-i-pack
puts [255,255,0,0].pack("c*") # c = 8-bit unsigned int, * = repeat for every element

# & | ^ bitwise operations
puts "Bitwise:"
puts 0b1000 & 0b1000 # 8
puts 0b1000 & 0b0000 # 0
puts 0b1111 & 0b0001 # 1
# https://apidock.com/ruby/String/unpack
# "abc \0\0abc \0\0".unpack('A6Z6')   #=> ["abc", "abc "]
# "abc \0\0".unpack('a3a3')           #=> ["abc", " \000\000"]
# "abc \0abc \0".unpack('Z*Z*')       #=> ["abc ", "abc "]
# "aa".unpack('b8B8')                 #=> ["10000110", "01100001"]
# "aaa".unpack('h2H2c')               #=> ["16", "61", 97]
# "\xfe\xff\xfe\xff".unpack('sS')     #=> [-2, 65534]
# "now=20is".unpack('M*')             #=> ["now is"]
# "whole".unpack('xax2aX2aX1aX2a')    #=> ["h", "e", "l", "l", "o"]
#
#
# # There's also an 'm' format that we can use for fast base64 encoding:
# ["Hello, world"].pack("m0") #=> 'SGVsbG8sIHdvcmxk'