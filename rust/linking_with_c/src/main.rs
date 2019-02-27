extern crate libc;

use libc::c_int;

#[link(name="multiply")]
extern {
    fn multiply(x: c_int, y: c_int) -> c_int;
}

fn main() {
    let product= unsafe { multiply(6, 4) };
    println!("{}", product);
}
