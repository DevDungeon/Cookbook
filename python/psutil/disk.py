import psutil


print(psutil.disk_partitions())

print(psutil.disk_usage('/'))

print psutil.disk_io_counters(perdisk=False)
