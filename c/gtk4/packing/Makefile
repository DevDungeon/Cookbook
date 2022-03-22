all: main

main: main.c
	gcc -o main `pkg-config --cflags gtk4` main.c `pkg-config --libs gtk4`

clean:
	rm a.out

