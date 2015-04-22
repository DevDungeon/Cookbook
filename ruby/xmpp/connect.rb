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
    jid = JID.new(@jabber_id, @password)
    @client = Client.new jid
    @client.connect
    @client.auth @jabber_password
    @client.send(Presence.new.set_type(:available))
    puts "Hurray...!!  Connected..!!"
  end
end

Bot.new('nanobot@devdungeon.com').connect
