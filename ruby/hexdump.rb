# Take contents from STDIN or file and dump out as hex
# e.g.
# 2043 6C69 636B 2074 6865 2073 6561 7263
# 6820 6275 7474 6F6E 0A65 6C65 6D65 6E74

ARGF.binmode

consecutive_print_count = 0
prints_per_line = 0

# until ARGF.eof?
    # ch = ARGF.readbyte
ARGF.each_byte do |ch|
    printf("%02X", ch)

    consecutive_print_count += 1
    prints_per_line += 1
    if consecutive_print_count == 2
        if prints_per_line == 16
            printf("\n")
            prints_per_line = 0
        else
            printf(" ")
        end
        consecutive_print_count = 0
    end

end
