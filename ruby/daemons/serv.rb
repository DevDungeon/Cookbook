x = 0
while true
	File.open(File.dirname(__FILE__) + "/out.dat", 'w') { |file| file.write(x) }
	x += 1
	sleep 2
end