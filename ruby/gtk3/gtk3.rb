#!/usr/bin/ruby

'''
GTK3 Example
Requires: gem install gtk3
'''

require 'gtk3'

class MyApp < Gtk::Window

	def initialize
		super

		set_title "Window Title"

		signal_connect "destroy" do
			Gtk.main_quit
		end

		set_default_size 400, 200

		set_window_position Gtk::Window::Position::CENTER

		show
	end
end

#Gtk.init
window = MyApp.new
Gtk.main

