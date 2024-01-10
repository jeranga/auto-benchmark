# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script allows for automatic clicking when the mouse hovers over a pixel of a specified color.
# It continuously checks the color of the pixel under the mouse pointer and performs a click if the color matches the target color.
# A mouse click event resets this check, allowing for repeated use.

import threading
import pyautogui
from pynput import mouse

# Define the target color (RGB) for the pixel check
target_color = (119, 216, 119)

# Event flag to control the pixel checking thread
click_event = threading.Event()

def check_pixel_color():
    """Check the pixel color under the mouse and click if it matches the target color."""
    while not click_event.is_set():
        x, y = pyautogui.position()
        pixel = pyautogui.pixel(x, y)
        if pixel == target_color:
            pyautogui.click()
            click_event.set()  # Stop the script after clicking

def on_click(x, y, button, pressed):
    """Handle mouse clicks to reset the pixel checking thread."""
    if pressed:
        click_event.clear()
        threading.Thread(target=check_pixel_color).start()

# Set up a listener for mouse click events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
