use std::env;
use std::fs;
use std::io::Read;

fn check_arguments() -> String {
    // Take a filename as the first CLI argument
    let args: Vec<String> = env::args().collect();

    let filename = args.get(1);

    if filename.is_none() {
        println!("No filename arg provided.");
        print_usage(args.get(0).unwrap());
        std::process::exit(1);
    }
    return filename.unwrap().to_owned();
}

fn print_usage(executable_filename: &String) {
    println!("Usage: ");
    println!(" {} <filename>", executable_filename);
    println!("Example: ");
    println!(" {} ~/.ssh/config", executable_filename);
}

fn main() {
    let filename = check_arguments();
    let mut buffer = [0; 8];
    let mut keep_running = true;
    let mut column = 0;

    // Open the file
    let open_file = fs::File::open(filename.clone());
    if open_file.is_err() {
        println!("Unable to open file: {}", filename);
        std::process::exit(1);
    }
    let mut file = open_file.unwrap();

    while keep_running {
        let data = file.read(&mut buffer);
        if data.is_ok() {
            // Exit infinite loop once no more bytes to read
            if data.unwrap() == 0 {
                keep_running = false;
            }

            // Print the hex values
            for i in 0..buffer.len() {
                if buffer[i] < 16 {
                    print!("0");
                }
                print!("{:X} ", buffer[i]); // x: i32
                column = column + 1;
                if column > 7 {
                    column = 0;
                    print!("\n");
                }
            }
        } else {
            keep_running = false;
        }
    }
}
