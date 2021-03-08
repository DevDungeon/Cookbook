require 'snoo'

reddit = Snoo::Client.new
reddit.log_in("user", "pass")
reddit.log_out