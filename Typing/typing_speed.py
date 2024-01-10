# Author: [Your Name]
# Date of Creation: [Today's Date]
# Last Edited: [Today's Date]
#
# Description:
# This script allows the user to set a region of the screen by clicking and dragging the mouse.
# Once the region is set, it captures a screenshot of this region.
# The script then uses OCR (Optical Character Recognition) via pytesseract to extract text from the screenshot.
# The extracted text is cleaned, optionally stripped of a leading '|', saved as an image, and then typed out.
# This can be useful for various tasks like copying text from images or areas where text selection is not possible.

import pytesseract
import pyautogui
from pynput import mouse
import math

# Initialize coordinates for the region of interest on the screen
px, py, rx, ry = 0, 0, 0, 0

def strip(value):
    """Remove new lines and returns from the string."""
    return ''.join(value.splitlines())

def on_click(x, y, button, pressed):
    """Handles mouse click events to set the region of interest."""
    global px, py, rx, ry
    if pressed:
        px, py = math.ceil(x), math.ceil(y)
    else:
        rx, ry = math.ceil(x), math.ceil(y)
        return False  # Stop listener

def begin_automation():
    """Captures screenshot and processes it with OCR."""
    pic = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
    text = pytesseract.image_to_string(pic, lang='eng', config='--psm 6 --oem 3')
    cleaned_text = text.replace('\n', ' ').replace('\r', '')
    pic.save("pic.png")

    # Type out the cleaned text, skipping the first character if it is '|'
    pyautogui.write(strip(cleaned_text[1:]) if cleaned_text.startswith('|') or cleaned_text.startswith('[') else strip(cleaned_text))
    print(strip(text))

# Start the mouse listener to select a region on the screen
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Begin the screenshot and OCR automation after the region is selected
begin_automation()
