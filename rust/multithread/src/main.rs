use std::thread;
use std::time;

fn main() {
    println!("Starting application...");

    let thread_join_handle = thread::spawn(|| {
        println!("Hello!");
        thread::sleep(time::Duration::from_millis(1000));
        println!("Hello!");
        return "Thread return value"
    });

    println!("All threads launched. Waiting for completion.");
    let result = thread_join_handle.join();

    println!("Thread has completed. Result:");
    println!("{:?}", result.unwrap());
}

