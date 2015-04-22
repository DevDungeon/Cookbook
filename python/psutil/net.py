import psutil

print(psutil.net_io_counters(pernic=True))


# Prints inet by default
print(psutil.net_connections())

# different kind values
print(psutil.net_connections(kind='tcp'))

#Kinds:
# inet, inet4, inet6, tcp, tcp4, tcp6, udp, udp4, udp6, unix, all

