require 'xmpp4r'
require 'xmpp4r/client'
include Jabber

class Bot

  attr_reader :client

  def initialize jabber_id
    @jabber_id = jabber_id
    @jabber_password = ENV['jabber_password']

    

  end

  def connect
    jid = JID.new(@jabber_id)
    @client = Client.new jid
    @client.connect
    @client.auth @jabber_password
    @client.send(Presence.new.set_type(:available))
  end

  def send_message
    message = Message.new("nanodano@devdungeon.com", "Hello, world!")
    message.type=:chat
    @client.send(message)
  end


	


end

bot = Bot.new('nanobot@devdungeon.com')
bot.connect
bot.send_message

# Add a callback handler
	bot.client.add_message_callback do |message|
		unless message.body.nil? && message.type != :error
		puts "Received message: #{message.body}"
		# Echo the received message back to the sender
		reply = Message.new(message.from, message.body)
		reply.type = message.type
		@client.send(reply)
		end
	end

while true
end