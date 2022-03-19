#g++ windows.cpp -lncurses

g++ windows.cpp -lncurses -L$HOME/.local/lib -I$HOME/.local/include{,/ncurses}
