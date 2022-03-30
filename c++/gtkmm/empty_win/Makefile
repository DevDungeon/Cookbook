
build:
	g++ main.cpp -L/usr/local/lib `pkg-config gtkmm-4.0 --cflags --libs` -std=c++20

build-static:
	LD_LIBRARY_PATH=/usr/local/lib g++ main.cpp -L/usr/local/lib `pkg-config gtkmm-4.0 --cflags --libs` -std=c++20 -static

clean:
	rm a.out

run:
	LD_LIBRARY_PATH=/usr/local/lib ./a.out
