# In bash
# export VAR=val

# In windows
# set VAR=value

# Print some variables
puts ENV['PATH']
puts ENV['EDITOR']

# Change a variable then launch a new program
ENV['EDITOR'] = 'gedit'
puts ENV['EDITOR']
