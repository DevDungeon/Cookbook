# check if files are different
# if they are different, print out what byte they are different at

if ARGV.length != 2
    puts "[-] Expected exactly two file names as arguments."
    exit -1
end

puts "[*] Checking if #{ARGV[0]} is identical to #{ARGV[1]}"
puts "[*] Identical? #{File.identical?(ARGV[0], ARGV[1])}"