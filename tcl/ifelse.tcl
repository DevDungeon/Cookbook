#!/bin/env tclsh
puts "Guess a number"
set number 5

gets stdin guess
if {$guess != $number} {
    puts "Incorrect guess. Number is $number"
} else { # elseif
    puts "You guessed correct!"
}
