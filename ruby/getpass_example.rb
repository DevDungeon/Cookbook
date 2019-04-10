require 'io/console'

# In Ruby 2.3+ use IO::console.getpass
# The prompt is optional
password = IO::console.getpass "Enter Password: "
puts "Your password was #{password.length} characters long."


# Another option using $stdin.noecho()
$stdout.print "Enter password: "
password = $stdin.noecho(&:gets)
password.strip!
puts "\nYour password was #{password.length} characters long."
