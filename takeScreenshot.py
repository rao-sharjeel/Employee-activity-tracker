import numpy as np
import cv2
import pyautogui
import datetime

def take_screenshot():  
    try:
        # take screenshot using pyautogui
        image = pyautogui.screenshot()
        
        # since the pyautogui takes as a 
        # PIL(pillow) and in RGB we need to 
        # convert it to numpy array and BGR 
        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)
        # Getting current time
        current_time = datetime.datetime.now().strftime("%H-%M-%S")

        # writing it to the disk using opencv
        cv2.imwrite(f"screenshots/{str(current_time)}.png", image)
    except:
        return 0
    return 1