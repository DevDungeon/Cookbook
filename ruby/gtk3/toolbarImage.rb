#!/usr/bin/ruby

'''
ZetCode Ruby GTK tutorial

This example creates a simple toolbar.

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
    
        toolbar = Gtk::Toolbar.new
        toolbar.set_toolbar_style Gtk::Toolbar::Style::ICONS

        newtb = Gtk::ToolButton.new :stock_id => Gtk::Stock::NEW
        opentb = Gtk::ToolButton.new :stock_id => Gtk::Stock::OPEN
        savetb = Gtk::ToolButton.new :stock_id => Gtk::Stock::SAVE
        sep = Gtk::SeparatorToolItem.new
        quittb = Gtk::ToolButton.new :stock_id => Gtk::Stock::QUIT
       
        toolbar.insert newtb, 0
        toolbar.insert opentb, 1
        toolbar.insert savetb, 2
        toolbar.insert sep, 3
        toolbar.insert quittb, 4
        
        quittb.signal_connect "clicked" do
            Gtk.main_quit
        end

        vbox = Gtk::Box.new :vertical, 2
        vbox.pack_start toolbar, :expand => false, 
            :fill => false, :padding => 0

        add vbox
        
        set_title "Toolbar"
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
