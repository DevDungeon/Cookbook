#!/usr/bin/ruby

'''
ZetCode Ruby GTK tutorial

This example creates a simple menubar.

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

        override_background_color :normal, 
            Gdk::RGBA.new(0.2, 0.2, 0.2, 1)
        
        mb = Gtk::MenuBar.new

        filemenu = Gtk::Menu.new
        filem = Gtk::MenuItem.new "File"
        filem.set_submenu filemenu
       
        exit = Gtk::MenuItem.new "Exit"
        exit.signal_connect "activate" do
            Gtk.main_quit
        end
        
        filemenu.append exit

        mb.append filem

        vbox = Gtk::Box.new :vertical, 2

        vbox.pack_start mb, :expand => false, 
            :fill => false, :padding => 0

        add vbox
        
        set_title "Simple menubar"
        signal_connect "destroy" do 
            Gtk.main_quit 
        end        

        set_default_size 300, 200
        set_window_position :center
        
        show_all        
    end
end

Gtk.init
    window = RubyApp.new
Gtk.main   
