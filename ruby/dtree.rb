#!/usr/bin/ruby
# Similar to `tree` on Linux

# Check for no args
if ARGV.length == 0
    puts "[-] No arguments provided. Provide a directory."
    exit -1
end

# Make sure arg provided is a directory
unless File.directory?(ARGV[0])
    puts "[-] Value provided is not a directory: #{ARGV[0]}"
    exit -1
end

Dir.entries(ARGV[0]).each do |entry|
    if File.directory? entry
        puts "#{entry}" + File::SEPARATOR
    elsif File.file? entry
        puts "#{entry}"
    else
        puts " [Not a file or a dir?] #{entry}"
    end
end
