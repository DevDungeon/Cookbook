==========
Rust Notes
==========

Option 1) Install with rustup:

  curl https://sh.rustup.rs -sSf | sh
  # Don't forget to update the PATH (~/.cargo/bin)

Option 2) Installing compiler with apt:

  sudo apt-get install rustc

Start a new project:

  cargo new ~/myproject

Run a project:

  # From the project directory
  cargo run

Get docs with:

  rustup doc


Useful Links
============

Documentation: https://doc.rust-lang.org/book/index.html
Getting started: https://www.rust-lang.org/learn/get-started
Package repository: https://crates.io/
Awesome Rust: https://github.com/rust-unofficial/awesome-rust


Topics
======

x Hello, world
x Adding dependencies
x Getting user input from stdin
x Taking command line arguments
x Reading and writing files
x TCP client/server
x Making HTTP requests
x Parsing JSON
x Packet capturing
  Packaging modules/publishing
  Creating a CSV file
  Making database connections
  Wrapping C libraries
  Can you link Rust object files with C? - Yes!
  Playing an audio file
  Multithreading
  Drawing 2D graphics to screen
  Drawing 3D graphics to screen
  GUI programming
