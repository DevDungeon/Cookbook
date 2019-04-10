//extern crate std;

use std::io;

fn main() {
    println!("Hello, world!");

    let mut user_text = String::new();

    io::stdin().read_line(&mut user_text)
        .expect("Failed to read line");

    println!("You said: {}", user_text);
}
