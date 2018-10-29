# Execute another command
# http://ruby-doc.org/core-2.5.3/Kernel.html#method-i-exec
# http://ruby-doc.org/core-2.5.3/Kernel.html#method-i-system
#
#
# Options:
# Process.exec()
# Kernel.system() # Executes a command in subshell. returns true on 0 exit status, false on non-zero, nil if failed. Error avail in $?
# `` # returns output, sets $? with return value
# %x()  # same as backticks
# # IO.popen??
# Kernel.spawn ?
#
# $?.exitstatus

# Execute a command in the shell and store results
puts `dir`
puts "But I still maintain control afterwards"


# `cmd` → string click to toggle source
# Returns the standard output of running cmd in a subshell. The built-in syntax %x{...} uses this method. Sets $? to the process status.
#
#     `date`                   #=> "Wed Apr  9 08:56:30 CDT 2003\n"
# `ls testdir`.split[1]    #=> "main.rb"
# `echo oops && exit 99`   #=> "oops\n"
# $?.exitstatus            #=> 99


puts Kernel.system("echo hi")
puts Kernel.system("echo", "hi")


# System executes in a subshell

# Exec hands off control, including stdout and all
# process is completely replaced
Process.exec("dir /p")



