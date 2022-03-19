SHELL=/bin/bash

all: clean static shared run

static:
	# Build static binary with libdano.a
	g++ -o hello-static main.cpp -I../include -L../lib -ldano -static

shared:
	# Dynamically link against libdano.so
	g++ -o hello-dyn main.cpp -I../include -L../lib -ldano

clean:
	if [[ -f a.out ]]; then rm a.out; fi
	if [[ -f hello-static ]]; then rm hello-static; fi
	if [[ -f hello-dyn ]]; then rm hello-dyn; fi

run:
	./hello-static
	LD_LIBRARY_PATH=../lib ./hello-dyn
