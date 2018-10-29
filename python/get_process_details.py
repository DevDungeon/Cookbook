import psutil
import colorama

# This takes a while....thread it?

pids = psutil.pids()
print(pids)

# add --summary to get just the names
summary = False


# Will get permission denied for most processes
for pid in pids:
    try:
        p = psutil.Process(pid)

        if summary:
            print ("%d\t%s" % (pid, p.name()))
            continue
            
        print("========== pid %d ==============" % pid)
        print(p.id())
        print(p.name())
        print(p.exe())
        print(p.cwd())
        print(p.cmdline())
        print(p.status())
        print(p.username())
        try:
            print(p.terminal())
        except:
            print("No terminal.")
        

        print("UIDS: %s ")
        try:
            print(p.uids())
        except:
            print("No UIDS")

        print("GIDS:")
        try:
            print(p.gids())
        except:
            print("No GIDS")


        print(p.cpu_times())
        #print(p.cpu_percent(interval=1.0))
        print(p.cpu_percent())
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

        print("Number of file descriptors:")
        try:
            print(p.num_fds())
        except Exception as e:
            print("No num_fds")

        print("Threads:")
        print(p.threads())
        print(p.num_ctx_switches())
        
        print("Nice:")
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
        print("++++++++++++ Completed dumping pid %d +++++++++++++" % pid)
    except Exception as e:
        print("")
        print("======================================== [-] ==> Error with pid: %d - %s" % (pid, e))


