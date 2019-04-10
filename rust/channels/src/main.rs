use std::sync::mpsc;
use std::thread;
use std::time;

fn main() {
    let (transmit, receive) = mpsc::channel();

    let sending_thread = thread::spawn(move || {
        println!("Sending data in to channel...");
        thread::sleep(time::Duration::from_secs(2));
        transmit.send(123);
        thread::sleep(time::Duration::from_secs(2));
        transmit.send(333);
    });

    let receiving_thread = thread::spawn(move || {
        println!("Waiting to receive data...");
        println!("{:?}", receive.recv().unwrap());
        println!("{:?}", receive.recv().unwrap());
    });

    receiving_thread.join().unwrap();
}
