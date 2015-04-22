require 'mumble-ruby'


# Configure all clients globally
Mumble.configure do |conf|
    # sample rate of sound (48 khz recommended)
    conf.sample_rate = 48000
    # bitrate of sound (32 kbit/s recommended)
    conf.bitrate = 32000
    # Find/generate certs location - creats folder for each user
    # conf.ssl_cert_opts[:cert_dir] = File.expand_path("./")
end

# Set or override global 
cli = Mumble::Client.new('devdungeon.com') do |conf|
	conf.username = "Bot"
	conf.password = ""
end

# Set a callback to handle incoming text messages
cli.on_text_message do |msg|
	# Just print incoming message object to console
	puts msg
	#puts msg.message
end

# Actual connect
cli.connect
# Without sleep, next commands get run before conn established
sleep 2

#cli.mute
#cli.deafen

cli.join_channel("The Quiet Room") # Room ID or name


puts "Channels ========================"
cli.channels.each do |chan|
	puts chan.name
end

puts "Users ==========================="
cli.users.each do |user|
	puts user.name
end

cli.text_user('NanoDano', 'Hello from the Ruby bot!')
sleep 2

#cli.text_channel_img("The Blind Tiger", "image.png")

sleep 2
#cli.stream_raw_audio("file.fifo") # raw PCM data

while true
	# Just stay online until interrupted
end

cli.disconnect