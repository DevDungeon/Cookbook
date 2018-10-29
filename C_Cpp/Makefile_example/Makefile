# By default running make with no args runs first make rule

# make       # or
# make my_custom_make  

# make debug
# make release
# make clean

my_custom_make:
	g++ main.cpp -o main -Wall -g

debug:
	g++ main.cpp -Wall -g

release:
	g++ main.cpp -Wall -static

clean:
	rm main

