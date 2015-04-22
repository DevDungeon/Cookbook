#!/usr/bin/ruby

dirs = Dir.entries "/"

print dirs

dirs.each { |dir| print dir + "\n" }