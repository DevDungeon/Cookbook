use std::fs;
use std::fs::File;
use std::error::Error;
use std::path::Path;
use std::io::prelude::*;

static TEXT: &'static str =
"hello,
multi-line text
123
";

fn main() {
    // Write a file
    { // Creates a scope?
        let filepath = Path::new("/home/nanodano/test.txt");
        
        let mut file = match File::create(&filepath) {
            Err(why) => panic!("Couldn't create file: {}", why.description()),
            Ok(file) => file,
        };

        // Or write_all(b"string as bytes")
        match file.write_all(TEXT.as_bytes()) {
            Err(why) => panic!("Couldn't write: {}", why.description()),
            Ok(_) => (),
        };
    }
   
    // Read a file
    let contents = fs::read_to_string("/home/nanodano/test.txt")
        .expect("Something went wrong reading the file");

    println!("{}", contents)

}
