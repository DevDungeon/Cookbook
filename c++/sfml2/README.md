# SFML 2


https://www.sfml-dev.org/


## Documentation



https://www.sfml-dev.org/ - On the official website there are online tutorials and references. You can also download HTML documentation as a zip from their download page. Additionally, download the source code zip which contains a directory of `examples/`.

- https://www.sfml-dev.org/files/SFML-2.5.1-sources.zip
- https://www.sfml-dev.org/files/SFML-2.5.1-doc.zip
- https://www.sfml-dev.org/learn.php

## Installation

### Debian

To install SFML 2 on Debian:

```bash
sudo apt install libsfml-{audio2.5,dev,doc,graphics2.5,network2.5,system2.5,window2.5}
```

### Build from source

```bash
# Download from https://www.sfml-dev.org/
wget https://www.sfml-dev.org/files/SFML-2.5.1-sources.zip
wget https://www.sfml-dev.org/files/SFML-2.5.1-doc.zip

# May need to install some additional dependencies to compile
sudo apt install libudev{1,-dev}
sudo apt install libopenal-dev

# After unzipping and moving into sources dir
cmake .
make help
make
# Optional to install
make install/local

# After building, you will have:
lib/      # .so shared libraries
include/  # header files
examples/ # Reference code
tools/    # pkg-config files, android/xcode stuff
src/      # Original sources
```

## Compiling and linking apps

```bash
# If your SFML is in a standard location
g++ -c main.cpp
g++ main.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system

# If your SFML is in a special location, specify
# the include and library paths
g++ -c main.cpp -I<sfml-install-path>/include
g++ main.o -o sfml-app -L<sfml-install-path>/lib -lsfml-graphics -lsfml-window -lsfml-system
```

## Docs

To build docs, go into `docs/`and run `doxygen` to get the HTML files.

