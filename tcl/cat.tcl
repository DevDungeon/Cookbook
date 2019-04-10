#!/bin/env tclsh
set file [open [lindex $argv 0] r]
set input [read $file]
set lines [split $input "\n"]
foreach line $lines {
#	# Do something with line and print it to stdout
   puts $line
}
close $file
