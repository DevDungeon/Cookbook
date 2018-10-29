# Similar to `head` linux program
# Prints first n lines of stdin
# Example usage to print out first 4 lines only:
# cat file.txt | ruby head.rb 4

max_lines = ARGV[0].to_i

lines_printed = 0

STDIN.each do |line|
    puts line
    lines_printed += 1
    if lines_printed == max_lines
        break
    end
end