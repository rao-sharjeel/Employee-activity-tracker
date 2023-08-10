from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from getRunningApps import get_active_window_title, get_running_processes
from takeScreenshot import take_screenshot
import json
from datetime import datetime

TIME_INTERVAL = 60 #time interval in seconds after which screenshot and json will be created and API will be called.
POSTING_FLAG = 0 # 0 means we are currently not posting anything and only saving.

def save_to_file(filename, json_data):
    with open(f"jsons/{filename}", 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"JSON saved {filename}")
    print(f"Saved at {json_data}")

def post_json(json_data):
    print(f"Posting JSON data: {json_data}")

def post_screenshot(ss_name):
    print("Posting screenshot" + str(ss_name))

def make_json():

def focus_tracker():
    first_json_file = 'json_file_1.json'
    second_json_file = 'json_file_2.json'
    first_screenshot = 'ss_1.png'
    second_screenshot = 'ss_2.png'
    
    process_time={}
    timestamp = {}
    
    user_id = "234"
    counter = 0
    iteration = 0

    while True:
        try:
            current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        except:
            current_app = "undefined"
        timestamp[current_app] = int(time.time())
        # time.sleep(1)
        
        if current_app not in process_time.keys():
            process_time[current_app] = 0
        process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
        counter += 1
        print(process_time)
        
        if counter == TIME_INTERVAL: # 5th second data as interval is set to 5
            
            # JSON creation process starts here

            focused_apps_list = list(process_time.keys())
            focused_apps_list_renamed = [app.lower() for app in focused_apps_list]

            background_apps_list = get_running_processes()
            background_apps_list_renamed = [app.split(" ")[-1].lower() for app in background_apps_list]

            unused_apps = [app for app in background_apps_list_renamed if app not in focused_apps_list_renamed]
            unused_apps_zeros = [0] * len(unused_apps)
            unused_apps_dict = dict(zip(unused_apps, unused_apps_zeros))
            
            focused_keys = list(process_time.keys())
            focused_times = list(process_time.values())

            data = {}
            data["current_app"] = get_active_window_title()
            # data["focused_apps"] = process_time
            # data.update(unused_apps_dict)

            data_list = []
            for i in range(len(focused_keys)):
                data_list.append({'app_name': focused_keys[i], 'time': focused_times[i]})

            data['focused_apps'] = data_list
            data["background_apps"] = background_apps_list_renamed

            json_dict = {}
            json_dict["user_id"] = user_id
            json_dict["current_time"] = str(datetime.now())
            json_dict['data'] = data

            json_obj = json.dumps(json_dict, indent=4)
            # print(json_obj)

            # JSON Creation process ends here
            
            if iteration < 2: #first 2 times save only
                if iteration == 0:
                    save_to_file(first_json_file, json_obj)
                    screenshot_check = take_screenshot(first_screenshot)
                    if screenshot_check:
                        print("Screenshot Taken\n")
                    else:
                        print("Error with screenshot\n")
            
                else:
                    save_to_file(second_json_file, json_obj)        
                    screenshot_check = take_screenshot(second_screenshot)
                    if screenshot_check:
                        print(f"Screenshot Taken {first_screenshot}\n")
                    else:
                        print(f"Error with screenshot {second_screenshot}\n")
            
            else:
            # After 2 times, start posting JSON data from the files
                if iteration % 2 == 0:
                    with open(f"jsons/{first_json_file}", 'r') as f:
                        first_json_data = json.load(f)
                    post_json(first_json_data)
                    save_to_file(first_json_file, json_obj)
            
                    screenshot_check = take_screenshot(first_screenshot)
                    if screenshot_check:
                        print("Screenshot Taken\n")
                    else:
                        print("Error with screenshot\n")
            
                    iteration = 3
                else:
                    with open(second_json_file, 'r') as f:
                        second_json_data = json.load(f)
                    post_json(second_json_data)
                    save_to_file(second_json_file, json_obj)
                            
                    screenshot_check = take_screenshot(second_screenshot)
                    if screenshot_check:
                        print(f"Screenshot Taken {first_screenshot}\n")
                    else:
                        print(f"Error with screenshot {second_screenshot}\n")
            
                    iteration = 2

            counter = 0
            iteration += 1

            process_time={}
            timestamp = {}

# focus_tracker()