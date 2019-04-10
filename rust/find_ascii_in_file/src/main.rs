use std::env;
use std::fs::File;
use std::io::Read;

fn print_usage(executable_filename: &String) {
    println!("Usage: ");
    println!(" {} <filename>", executable_filename);
    println!("Example: ");
    println!(" {} ~/.ssh/config", executable_filename);
}

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

fn main() {
    let filename = check_arguments();
    let mut buffer = [0; 1024];

    let open_file_result = File::open(filename.clone());

    if open_file_result.is_err() {
        println!("[-] Error opening file: {}", filename);
        std::process::exit(1);
    }

    let mut open_file = open_file_result.unwrap();

    while true {
        let data = open_file.read(&mut buffer);
        if data.is_ok() {
            // Exit infinite loop once no more bytes to read
            let num_bytes_read = data.unwrap();
            if num_bytes_read == 0 {
                break; // Can we break directly instead of using the bool var?
            }

            let mut last_char_was_ascii= false;
            for i in 0..num_bytes_read {
                // TODO add a flag to skip spaces, then ignore ascii 32
                if buffer[i] >= 33 && buffer[i] <= 126 {
                    if !last_char_was_ascii {
                        print!(" ");
                        last_char_was_ascii = true;
                    }
                    print!("{}", buffer[i] as char)
                }
            }

        } else {
            break;
        }
    }
}
