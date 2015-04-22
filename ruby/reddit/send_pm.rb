require 'snoo'

reddit = Snoo::Client.new

reddit.log_in("user", "pass")

puts reddit.send_pm("user", "subject", "message")

reddit.log_out