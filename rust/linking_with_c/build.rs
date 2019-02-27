fn main() {
    println!("cargo:rustc-link-search=native=/home/nanodano/cookbook/rust/linking_with_c/c_library/");

    // Not required if the #[link(name="mutliply")] decorator is being used
    // in the main Rust file where it defines external functions
    //println!("cargo:rustc-link-lib=multiply");
}