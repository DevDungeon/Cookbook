Linking with C libraries in Rust
================================


To link with a c lib....
------------------------

Make the C library::

 gcc -c myfunctions.c -o myfunctions.o

Create the archive to make static lib (double check ubunut alias is not overriding)::

  ar libmyfunctions.a myfunctions.o

In the Rust file,

- Add all external functions at the top with ``extern{}`` block
- Add a link decorator like ``#[link(name = "myfunctions")]``
  + OR set the link in the build.rs file ``println!("cargo:rustc-link-lib=multiply");``
- Add ``extern crate libc;`` and ``use libc::c_int`` and all other datatypes needed
- When calling the C function, wrap in an ``unsafe{}`` block

Add a build.rs file for Cargo, and include::

  fn main() {
    println!("cargo:rustc-link-search=native=/path/to/dir/with_lib/");
  }

In the Cargo.toml file, add a dependency for::

  [dependencies]
  libc = "0.2.0"
