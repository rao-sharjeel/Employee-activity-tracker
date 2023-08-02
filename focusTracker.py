from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from getRunningApps import get_active_window_title, get_running_processes
from takeScreenshot import take_screenshot
import json
from datetime import datetime

process_time={}
timestamp = {}
user_id = "234"
counter = 0
while True:
    current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    print(GetForegroundWindow())
    print(win32process.GetWindowThreadProcessId(GetForegroundWindow()))
    print(psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]))
    timestamp[current_app] = int(time.time())
    time.sleep(1)
    if current_app not in process_time.keys():
        process_time[current_app] = 0
    process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    counter += 1
    # print(process_time)
    if counter == 10:
        counter = 0
        
        data = {}
        data["focused_apps"] = process_time
        data["background_apps"] = get_running_processes()
        data["current_app"] = get_active_window_title() 

        json_dict = {}
        json_dict["user_id"] = user_id
        json_dict["current_time"] = str(datetime.now())
        json_dict['data'] = data

        json_obj = json.dumps(json_dict, indent=4)
        print(json_obj)

        screenshot_check = take_screenshot()
        if screenshot_check:
            print("Screenshot Taken\n")
        else:
            print("Error with screenshot\n")
        process_time={}
        timestamp = {}