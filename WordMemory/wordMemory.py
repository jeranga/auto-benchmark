# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script captures screenshots of a specified screen region, extracts text using OCR (Tesseract),
# and performs automated mouse clicks based on the presence of new words. 
# It runs continuously, updating a set of words extracted from each screenshot and 
# clicking on predefined screen positions based on whether new words are detected.

import pytesseract
import pyautogui
from pynput import mouse
import time

# Coordinates for the region of interest on the screen
px, py, rx, ry = 1126, 390, 1758, 510

def on_click(x, y, button, pressed):
    """Function to handle mouse click events."""
    if pressed:
        words = set()
        size = 0
        screenshot_counter = 0

        while True:
            # Capture a screenshot of the defined region
            pic = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
            screenshot_counter += 1
            text = pytesseract.image_to_string(pic, lang='eng', config='--psm 6 --oem 3')

            # Process the extracted text
            words.add(text)
            print(f'Attempting to add "{text}" to set: {words}')
            newSize = len(words)

            if newSize > size:
                # If a new word is detected, click at a specific location
                pyautogui.click(1505, 550)
                size += 1
                print("Added!")
            else:
                # If no new word is detected, click at a different location
                pyautogui.click(1370, 550)
                print("Not added")

            # Manage timing for screenshot capture
            time.sleep(0.01)
            if screenshot_counter % 50 == 0:
                time.sleep(10)

# Set up a listener for mouse click events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
