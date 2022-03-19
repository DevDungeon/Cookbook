SHELL:=/bin/bash

all: static shared


static:
	echo "Building static library libdano.a"
	g++ -c src/functions.cpp -o obj/functions.o
	ar rcs lib/libdano.a obj/functions.o
	
shared:
	echo "Building shared library libdano.so"
	g++ -fPIC -c src/functions.cpp -o obj/functions.o
	g++ -shared -o lib/libdano.so obj/functions.o


clean:
	rm lib/*
	rm obj/*

