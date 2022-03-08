# Example `meson.build` file

# Run with:
# meson compile

# Follow the tutorial at
# https://mesonbuild.com/Tutorial.html

# `pip install meson` or `apt install meson`

project('example', 'c')  # https://mesonbuild.com/Reference-manual_functions.html#project

# Pass deps the value you would pass to `pkgconfig`
gtkdeps = [dependency('gtk+-3.0')]  # https://mesonbuild.com/Reference-manual_functions.html#dependency
executable('a.out', 'main.c', dependencies : gtkdeps)  # https://mesonbuild.com/Reference-manual_functions.html#executable

# On first run:
# meson setup builddir

# Then to do final compile:

# cd builddir
# ninja # apt install ninja
# ./a.out


############################
# To compile an existing project like GLib

# Setup builddir with prefix
# meson --prefix /path/to/install --buildtype=plain builddir

# To get config options
# meson configure

# To set config options:
# meson -Dsome_option=true --prefix /opt/abc builddir


# meson compile -C builddir
# meson test -C builddir




