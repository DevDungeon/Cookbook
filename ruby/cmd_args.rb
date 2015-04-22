#!/usr/bin/env ruby

# Basic command arguments
# ARGV[0] is command after file name
puts ARGV[0]
ARGV.each do|a|
  puts "Argument: #{a}"
end