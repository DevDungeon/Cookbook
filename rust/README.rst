==========
Rust Notes
==========

Option 1) Install with rustup::

  curl https://sh.rustup.rs -sSf | sh
  # Don't forget to update the PATH (~/.cargo/bin)

Option 2) Installing compiler with apt::

  sudo apt-get install rustc

Start a new project::

  cargo new ~/myproject

Run a project::

  # From the project directory
  cargo run

Get docs with::

  rustup doc


Useful Links
============

- Documentation: https://doc.rust-lang.org/book/index.html
- Getting started: https://www.rust-lang.org/learn/get-started
- Package repository: https://crates.io/
- Awesome Rust: https://github.com/rust-unofficial/awesome-rust


Completed Topics
================

- Hello, world
- Adding dependencies
- Getting user input from stdin
- Taking command line arguments
- Reading and writing files
- TCP client/server
- Making HTTP requests
- Parsing JSON
- Packet capturing

- Cross-compiling - https://github.com/japaric/rust-cross
- Wrapping C libraries
- Linking to custom C libraries
- Multithreading

Unfinished Topics
=================

- Channels
- Thread pools

- Packaging modules/publishing

- Creating a CSV file
- Making database connections

- Playing an audio file
- Drawing 2D graphics to screen
- Drawing 3D graphics to screen
- GUI programming
