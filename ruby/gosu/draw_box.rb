require 'rubygems'
require 'gosu'

class MyWin < Gosu::Window

	TOP_COLOR = Gosu::Color.new(0xFF1EB1FA)
	BOTTOM_COLOR = Gosu::Color.new(0xFF1D4DB5)

	def initialize
		super(640, 480, false)
		self.caption = "Window Title"
		@last_frame = Gosu::milliseconds
	end

	def update
		calculate_delta
	end

	def calculate_delta
		@this_frame = Gosu::milliseconds
		@delta = (@this_frame - @last_frame) / 1000.0
		@last_frame = @this_frame
	end

	def draw
		draw_background
	end

	def draw_background
		draw_quad(
			10, 10, TOP_COLOR,
			50, 10, TOP_COLOR,
			10, 100, BOTTOM_COLOR,
			50, 100, BOTTOM_COLOR,
			0)
	end
end

MyWin.new.show