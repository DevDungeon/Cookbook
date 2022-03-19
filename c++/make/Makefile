# By default running make with no args runs first make rule
SHELL := /bin/bash

all: clean debug run

debug:
	g++ main.cpp -Wall -g

release:
	g++ main.cpp -Wall -static

clean:
	if [[ -f main ]]; then rm main; fi

run:
	./a.out



