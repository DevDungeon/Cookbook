all: clean main

main: main.cpp
	g++ main.cpp -o interface -lncurses -L/home/odin/.local/lib -I/home/odin/.local/include

clean:
	if [ -f interface ]; then rm interface; fi;

