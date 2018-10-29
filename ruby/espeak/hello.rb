# gem install espeak-ruby
require 'espeak'
include ESpeak

# Simple text to speech
speech = Speech.new("Hello, world!")
speech.speak

# Creates audio file
speech = Speech.new("Hola mi amigo. Como estas?", voice: "es")
speech.save("hello-es.mp3") # invokes espeak + lame

# Lists languages
puts "Available languages:"
puts Voice.all.map { |v| v.language }.join(", ")

# Find particular voice
puts "English voice:"
puts Voice.find_by_language('en').inspect

# Change speech parameters
s = Speech.new("Zdravo svete", voice: "sr", pitch: 90, speed: 200)
s.speak