# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script automates the process of finding a specified target image on the screen and clicking at its center.
# The user defines a region of interest by clicking and dragging on the screen.
# The script takes a screenshot of this region, searches for the target image within it, and clicks at the center of the found target.

import cv2
import numpy as np
import pyautogui
import time
import sys
from PIL import ImageGrab
from pynput import mouse
import math

# Global variables to store the region coordinates
px, py, rx, ry = 0, 0, 0, 0
region_selected = False

def on_click(x, y, button, pressed):
    """Handles mouse click events to set the region of interest."""
    global px, py, rx, ry, region_selected
    if pressed:
        px, py = math.ceil(x), math.ceil(y)
    else:
        rx, ry = math.ceil(x), math.ceil(y)
        region_selected = True
        return False

# Initialize mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

# Load the target image
target_image_path = 'Targets/targetSC.png'
target = cv2.imread(target_image_path, cv2.IMREAD_UNCHANGED)
if target is None:
    print("Failed to load target image.")
    sys.exit()

# Process the target image
target_gray = cv2.cvtColor(cv2.resize(target, (0, 0), fx=0.5, fy=0.5), cv2.COLOR_BGR2GRAY)

def find_target_on_screen(target_gray, resize_factor=0.5):
    """Finds the target image on the screen and returns its location."""
    screenshot = ImageGrab.grab(bbox=(px, py, rx, ry))
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    resized_screenshot = cv2.resize(screenshot_gray, (0, 0), fx=resize_factor, fy=resize_factor)

    result = cv2.matchTemplate(resized_screenshot, target_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.7:
        target_w, target_h = target_gray.shape[::-1]
        return int(max_loc[0] / resize_factor), int(max_loc[1] / resize_factor), target_w, target_h

    return None, None, None, None

def main():
    """Main function to execute the target finding and clicking automation."""
    global region_selected
    while not region_selected:
        time.sleep(0.1)

    print("Starting automation...")
    while True:
        x, y, w, h = find_target_on_screen(target_gray)
        if x is not None and y is not None:
            pyautogui.moveTo(x + px + w // 2, y + py + h // 2)
            pyautogui.click()

if __name__ == '__main__':
    main()
