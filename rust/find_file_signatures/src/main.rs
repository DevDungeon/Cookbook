use std::env;
use std::fs::File;
use std::io::Read;
use std::collections::hash_map::HashMap;

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

    // TODO support signatures that are not only at the very beginning of a file
    let mut signatures: HashMap<&str, Vec<i32>>  = HashMap::new();
    signatures.insert("jpg1", [255, 216, 255, 219].to_vec() as Vec<i32>); // FF D8 FF DB
    signatures.insert("jpg2", vec![255, 216, 255, 224, 0, 16, 74, 70, 73, 70, 0, 1]); // FF D8 FF E0 00 10 4A 46 49 46 00 01
    signatures.insert("jpg3", vec![255, 216, 255, 225, -1, -1, 69, 120, 105, 102, 0, 0]); // FF D8 FF E1 -1 -1 45 78 69 66 00 00
    signatures.insert("png", vec![137, 80, 78, 71, 13, 10, 26, 10]); // 89 50 4E 47 0D 0A 1A 0A

    open_file.read(&mut buffer);

    for (filetype, signature_bytes) in signatures.iter() {

        let mut signature_matches = true;
//        println!("[*] Checking for: {}", filetype);

        for i in  0..signature_bytes.len() {
            // TODO add --debug or --verbose to toggle this output
//            println!("File byte:\t{:X}\tSignature byte:\t{:X}", buffer[i], signature_bytes[i]);
            if buffer[i] as i32 != signature_bytes[i] && signature_bytes[i] != -1{
                signature_matches = false;
            }
        }

        if signature_matches {
            println!("[+] Signature found: {}", filetype);
        } else {
//            println!("[-] Signature NOT found: {}", filetype);
        }
    }
}
