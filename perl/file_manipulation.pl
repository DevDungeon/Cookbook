# create Directory
mkdir /tmp/test

# Opening and Closing Files
$file = 'test.txt';

# open(INFO, $file);	# Open for input
open(INFO, ">$file");	# Open for output
# open(INFO, ">>$file");	# Open for appending
# open(INFO, "<$file");	# Also open for input

# close(INFO); # Close when complete


# Read lines of file in to array
# @lines = <INFO>;

# Print message to console for user
print STDOUT "Writing information to file.";
# Equivalent
print "Writing information to file.";


# Write string to file
print INFO "This line goes to the file.\n";

close(INFO)
