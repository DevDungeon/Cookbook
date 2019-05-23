#!/usr/bin/ruby

'''
ZetCode Ruby GTK tutorial

This program creates a quit
button. When we press the button,
the application terminates.

Author: Jan Bodnar
Website: www.zetcode.com
Last modified: May 2014
'''

require 'gtk3'

class RubyApp < Gtk::Window

    def initialize
        super

        init_ui
    end

    def init_ui

        fixed = Gtk::Fixed.new
        add fixed

        button = Gtk::Button.new :label => "Quit"
        button.set_size_request 80, 35
        button.signal_connect "clicked" do
            Gtk.main_quit
        end

        fixed.put button, 50, 50

        set_title  "Quit button"
        signal_connect "destroy" do
            Gtk.main_quit
        end

        set_default_size 300, 200
        set_window_position(:center)
        show_all
    end
end

#Gtk.init
window = RubyApp.new
Gtk.main
