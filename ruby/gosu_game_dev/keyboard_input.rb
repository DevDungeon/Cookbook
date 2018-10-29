require 'rubygems'
require 'gosu'

class MyWin < Gosu::Window
	def initialize
		super(640, 480, false)
		self.caption = "Window Title"
	end

	# Use the button_down event callback
	def button_down(id)
		case id
		when Gosu::KbEscape
			close
		end
	end

	# or use a manual check of button_down? during update
	def update
		if self.button_down?(Gosu::KbLeft)
      		close
      	end
    end
end

MyWin.new.show
