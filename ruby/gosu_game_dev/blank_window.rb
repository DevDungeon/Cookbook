require 'rubygems'
require 'gosu'

class MyWin < Gosu::Window
	def initialize
		super(640, 480, false)
		self.caption = "Window Title"
	end
end

MyWin.new.show
