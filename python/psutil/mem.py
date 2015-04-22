import psutil

# Print total, avail, percent, used, free, active, inactive, buffered, cache
print(psutil.virtual_memory())

# Print total, used, free, percent, sin, sout
print(psutil.swap_memory())

