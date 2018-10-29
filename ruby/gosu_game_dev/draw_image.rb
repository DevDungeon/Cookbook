require 'rubygems'
require 'gosu'

class MyWin < Gosu::Window

	TOP_COLOR = Gosu::Color.new(0xFF1EB1FA)
	BOTTOM_COLOR = Gosu::Color.new(0xFF1D4DB5)

	def initialize
		super(640, 480, false)
		self.caption = "Window Title"
		@image = Gosu::Image.new(self, 'logo.png', false)
	end

	def draw
		@image.draw(0, 0, 1)
	end

end

MyWin.new.show