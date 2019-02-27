Cross compiling with Rust
=========================

To cross-compile for Windows,
install the gcc cross-compiler and linker:

For example, in Ubuntu::

  sudo apt install gcc-mingw-w64{,-base}

Add the compile target with ``rustup``::

  rustup target add x86_64-pc-windows-gnu

Cross compile with --target=XX flag. For example::

  rustc --target=x86_64-pc-windows-gnu -C linker=x86_64-w64-mingw32-gcc test.rs
