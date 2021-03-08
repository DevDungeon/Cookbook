#!/usr/bin/ruby

'''
ZetCode Ruby GTK tutorial

This program shows a tooltip on 
a window and a button.

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
    
        set_title  "Tooltips"
        signal_connect "destroy" do 
            Gtk.main_quit 
        end
        
        fixed = Gtk::Fixed.new
        add fixed

        button = Gtk::Button.new :label =>'Button'
        button.set_size_request 80, 35      
        button.set_tooltip_text "Button widget"
  
        fixed.put button, 50, 50       

        set_tooltip_text "Window widget"
        set_default_size 300, 200
        set_window_position :center
        
        show_all
    end
end

Gtk.init
    window = RubyApp.new
Gtk.main
