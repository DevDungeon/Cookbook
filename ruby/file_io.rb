File.open("out.dat", 'w') { |file| 
	file.write("line 1\nline2\n")
}

File.open("out.dat", 'r').each_line do |line|
	puts line
end
