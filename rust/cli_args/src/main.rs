//extern crate std;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    println!("{:?}", args);
    println!("{}", &args[0]);

    // Will not panic if it doesn't exist
    let arg_five = args.get(5);
    if arg_five.is_none() { 
        println!("No fifth arg provided.")
    } else if arg_five.unwrap() == "five" {
        println!("Five is five!")
    } else {
        println!("Five is not five =(")
    }

    // "Debug format (:?) output
    println!("{:?}", arg_five);

    
}
