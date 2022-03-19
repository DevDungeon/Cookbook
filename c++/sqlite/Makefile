# /usr/include/sqlite3.h
# /usr/lib/x86_64-linux-gnu/libsqlite3.a

all: clean build

build:
	g++ -o sqlite_example sqlite_example.cpp -lsqlite3 -ldl -lpthread

clean:
	if [ -f sqlite_example ]; then rm sqlite_example; fi;
