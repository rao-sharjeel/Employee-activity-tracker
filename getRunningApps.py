import subprocess
import psutil
import win32gui
import time

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return title

def get_running_processes():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True)
    apps = []
    for line in proc.stdout:
        if not line.isspace():
            app_description = line.strip()
            apps.append(app_description)
    
    # active_window_title = get_active_window_title()
    # apps.append(f"Currently in focus: {active_window_title}")

    return apps[2:]

if __name__ == "__main__":
    time.sleep(1)
    running_processes = get_running_processes()
    for process in running_processes:
        print(process)




