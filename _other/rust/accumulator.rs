fn main() {
	let program = "+ + * - /";
	let mut acculumator = 0;

	for token in program.chars() {
		match token {
		'+' => accumulator += 1,
		'-' => accumulator -= 1,
		'*' => accumulator *= 2,
		'/' => accumulator /= 2,
		_ => {} // Ignore everything else
		}
	}
	println!("The program \"{}\" calculates to {}", program, accumulator);
}
