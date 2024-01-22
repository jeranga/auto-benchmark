# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script uses OCR (Optical Character Recognition) to read text from a specified screen region.
# After capturing the screen, it extracts numbers using pytesseract and performs automated clicks and keyboard actions.
# It's set to run continuously, increasing the delay between actions as it progresses.

import pytesseract
import pyautogui
from pynput import mouse
import time

# Coordinates for the region of interest on the screen
px, py, rx, ry = 0, 266, 2878, 620

def strip(value):
    """Remove newline characters from the string."""
    return ''.join(value.splitlines())

def on_click(x, y, button, pressed):
    """Function to handle mouse click events."""
    if pressed:
        time.sleep(0.5)
        timerog = 0.8
        timer = 1.8 
        level = 1

        while True:
            # Take a screenshot of the defined region
            pic = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
            # Extract text using pytesseract OCR
            text = pytesseract.image_to_string(pic, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
            pic.save("pic.png")
            # Perform automated actions based on the extracted text
            time.sleep(timer)
            level += 1
            timer = timerog * level
            pyautogui.click(1436, 483)
            pyautogui.write(strip(text))
            print("saw number: " + strip(text))
            pyautogui.click(1436, 582)
            time.sleep(1)
            pyautogui.click(1436, 620)
            time.sleep(1.0)

# Set up a listener for mouse click to trigger the automation
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
