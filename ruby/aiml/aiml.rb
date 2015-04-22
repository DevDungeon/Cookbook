require 'programr'

kernel = ProgramR::Facade.new

# Array of files or directories
aiml_files = Array.new()
aiml_files.push("aiml_files")

kernel.learn(aiml_files) # File or directory

while true
  print '>> '
  s = STDIN.gets.chomp
  reaction = kernel.get_reaction(s)
  STDOUT.puts "<< #{reaction}"
end