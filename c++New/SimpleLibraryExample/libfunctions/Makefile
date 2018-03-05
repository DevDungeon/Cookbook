
static:
	# Compile the library to an object file
	g++ -c src/functions.cpp -o obj/functions.o
	ar rcs lib/libfunctions.a obj/functions.o
	
shared:
	# Compile the library to be shared
	g++ -fpic -c src/functions.cpp -o obj/functions.o
	g++ -shared -o lib/libfunctions.so obj/functions.o


clean:
	rm lib/*
	rm obj/*

