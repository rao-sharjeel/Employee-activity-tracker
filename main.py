from getRunningApps import get_running_processes

apps = get_running_processes()
for line in apps[2:]:
    print(line.decode().rstrip())