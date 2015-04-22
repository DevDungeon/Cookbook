import psutil


pids = psutil.pids()
print(pids)

#p = psutil.Process(1234)
#p.name()

p = psutil.Process(pids[0])
# process name
print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.status())
print(p.username())
print(p.terminal())

print(p.uids())

print(p.gids())

print(p.cpu_times())
print(p.cpu_percent(interval=1.0))
print(p.cpu_affinity())
print(p.cpu_affinity([0]))
print(p.memory_percent())
print(p.memory_info())
#print(p.ext_memory_info())
print(p.memory_maps())
print(p.io_counters())
print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.num_fds())
print(p.threads())
print(p.num_ctx_switches())
print(p.nice())
#p.nice(10) #set

#p.ionice(psutil.IOPRIO_CLASS_IDLE) # Set IO Priority (win/lin)
#p.ionice()

#p.rlimit(psutil.RLIMIT_NOFILE, (5, 5)) # Linux set resource limits
#p.rlimit(psutil.RLIMIT_NOFILE)

#p.suspend()
#p.resume()

#p.terminate()
#p.wait(timeout=3)
#psutil.test()


