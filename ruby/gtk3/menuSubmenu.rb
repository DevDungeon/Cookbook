#!/usr/bin/ruby

'''
ZetCode Ruby GTK tutorial

This example shows a submenu.

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

        mb.append filem
        
        imenu = Gtk::Menu.new

        importm = Gtk::MenuItem.new "Import"
        importm.set_submenu imenu

        inews = Gtk::MenuItem.new "Import news feed..."
        ibookmarks = Gtk::MenuItem.new "Import bookmarks..."
        imail = Gtk::MenuItem.new "Import mail..."

        imenu.append inews
        imenu.append ibookmarks
        imenu.append imail

        filemenu.append importm
        
        exit = Gtk::MenuItem.new "Exit"
        exit.signal_connect "activate" do
            Gtk.main_quit
        end
        
        filemenu.append exit

        vbox = Gtk::Box.new :vertical, 2

        vbox.pack_start mb, :expand => false, 
            :fill => false, :padding => 0

        add vbox

        set_title "Submenu"
        signal_connect "destroy" do 
            Gtk.main_quit 
        end        

        set_default_size 350, 250
        set_window_position :center
        show_all        
    end
end

Gtk.init
    window = RubyApp.new
Gtk.main
