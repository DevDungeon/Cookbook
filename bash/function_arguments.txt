# Define a function
hello() {
	echo "Hello, world!"
}

# Run the function
hello

# Using function arguments
hello() {
	echo Nice to meet you, $1
}

# Represents all positiona parameters
$@

# Get all params from position 2
$@:2

# Start at the last positional parameter
${@: -1}