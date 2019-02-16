#!/bin/env tclsh

set x 100
puts $x

set X 50
puts $X

set "some number" 12345
puts ${some number}

puts [set "some number"]
