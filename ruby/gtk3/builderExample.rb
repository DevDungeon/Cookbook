#https://github.com/cedlemo/ruby-gtk3-tutorial/blob/1b395878c6d2bd8d26d716e27e34113e21069a18/samples/example-4.rb
require "gtk3"

#builder_file = "#{File.expand_path(File.dirname(__FILE__))}/builder.ui"
builder_file = "builder.glade"

# Construct a Gtk::Builder instance and load our UI description
builder = Gtk::Builder.new(:file => builder_file)

# Connect signal handlers to the constructed widgets
# window = builder.get_object("window1")
# window.signal_connect("destroy") { Gtk.main_quit }

# button = builder.get_object("button1")
# button.signal_connect("clicked") { puts "Hello World" }

# button = builder.get_object("button2")
# button.signal_connect("clicked") { puts "Hello World" }

# button = builder.get_object("quit")
# button.signal_connect("clicked") { Gtk.main_quit }

Gtk.main
