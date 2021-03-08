#gem install daemons
require 'daemons'

Daemons.run('my_service.rb')

#ruby daemonize.rb start
#ruby daemonize.rb stop
#ruby daemonize.rb run # Run without forking to background

# Passing arguments
# ruby daemonize.rb start -- --arg1=10 --arg2
# Accessible in ARGV
ARGV.each do |arg|
    puts arg
end
