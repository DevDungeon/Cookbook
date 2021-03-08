require 'rubygems'
require 'gosu'

class MyWin < Gosu::Window
	def initialize
		super(640, 480, false)
		self.caption = "Window Title"
	end

	# show cursor when inside window
	def needs_cursor?
		return true
	end
	# Could also be shortened as
	#def needs_cursor?; true; end


	# Use the button_down event callback
	def button_down(id)
		case id
		when Gosu::MsLeft
			puts "Left mouse button clicked at #{self.mouse_x}, #{self.mouse_y}"
		end
	end

	# or use a manual check of button_down? during update
	def update
		if self.button_down?(Gosu::MsRight)
      		puts "Right mouse button clicked at #{self.mouse_x}, #{self.mouse_y}"
      	end
    end
end

MyWin.new.show
