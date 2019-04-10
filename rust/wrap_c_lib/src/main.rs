extern crate libc;
use libc::size_t;

// In Ubuntu: sudo apt install libsnappy1v5 libsnappy-dev
#[link(name = "snappy")]
extern {
    fn snappy_max_compressed_length(source_length: size_t) -> size_t;
}

fn main() {
    let product = unsafe { snappy_max_compressed_length(64) };
    println!("{}", product);
}
