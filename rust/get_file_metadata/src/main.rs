// Print metadata about a filepath
extern crate chrono;
use std::env;
use std::fs::File;
use std::fs::Metadata;
use std::os::unix::fs::PermissionsExt;
use std::os::unix::fs::FileTypeExt;
use chrono::DateTime;
use chrono::Utc;

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

fn print_metadata(filename: &String, metadata: Metadata) {
    println!("[*] Metadata for file");
    println!("[*] =================");
    println!("[*] Name: {}", filename);
    println!("[*] Is block device: {:?}", metadata.file_type().is_block_device());
    println!("[*] Is char device: {:?}", metadata.file_type().is_char_device());
    println!("[*] Is FIFO: {:?}", metadata.file_type().is_fifo());
    println!("[*] Is socket: {:?}", metadata.file_type().is_socket());
//    println!("[*] Is symlink dir: {:?}", metadata.file_type().is_symlink_dir()); // Win only
//    println!("[*] Is symlink file: {:?}", metadata.file_type().is_symlink_file()); // Win only

    println!("[*] Is dir: {:?}", metadata.is_dir());
    println!("[*] Is file: {:?}", metadata.is_file());

    let permissions = metadata.permissions();
    println!("[*] Permissions: {:o}", permissions.mode());

    let modified = DateTime::<Utc>::from(metadata.modified().unwrap());
    let accessed = DateTime::<Utc>::from(metadata.accessed().unwrap());
    let format_string = "%Y-%m-%d %H:%M:%S UTC";
    println!("[*] Last modified: {}", modified.format(format_string).to_string());
    println!("[*] Last accessed: {}", accessed.format(format_string).to_string());
    if !metadata.created().is_err() {
        let created = DateTime::<Utc>::from(metadata.created().unwrap());
        println!("[*] Created: {}", created.format(format_string).to_string());
    } else {
        println!("[-] Created: N/A")
    }
}

fn main() -> std::io::Result<()> {
    // Get metadata for a file
    let filename: String = check_arguments();
    let file = File::open(&filename.to_owned())?;
    let metadata = file.metadata()?;
    print_metadata(&filename.to_owned(), metadata);
    return Ok(());
}
