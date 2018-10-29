# Get pid of current process

puts "My pid: #{Process.pid}"
puts "My parent pid: #{Process.ppid}"
# In Windows, find the name of a pid
# tasklist /fi "pid eq 4444"
#
puts "My group id: #{Process.gid}"
puts "My user id: #{Process.uid}"


original_pid = Process.pid

Process.fork
puts "My pid: #{Process.pid}"
puts "My parent pid: #{Process.ppid}"


# check if child pid?
# if child exec, replacing current process
#
# detach if you just wanted to fork and die(good for starting as a high priv to bind to a port and leaving child as low priv)
# https://ruby-doc.org/core-2.1.2/Process.html#method-c-detach
#
#
# https://ruby-doc.org/core-2.1.2/Process.html#method-c-clock_getres
# https://ruby-doc.org/core-2.1.2/Process.html#method-c-clock_gettime

# waitpid(pid=-1, flags=0) → fixnum
# Waits for a child process to exit, returns its process id, and sets $? to a Process::Status object containing information on that process. Which child it waits on depends on the value of pid:
#
# > 0
# Waits for the child whose process ID equals pid.
#
# 0
# Waits for any child whose process group ID equals that of the calling process.
#
# -1
# Waits for any child process (the default if no pid is given).
#
# < -1
# Waits for any child whose process group ID equals the absolute value of pid.
#
#
#
#
# time example
# fork,
#   if child process, exec(replacing self)
#   if parent, waitpid(child), keep track of time
# print time waited