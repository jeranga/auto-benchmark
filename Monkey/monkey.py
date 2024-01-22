# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script automates the task of identifying and clicking on numbered squares within a specified region on the screen.
# It takes screenshots, processes them to identify numbers using OCR, and performs clicks based on the identified number sequence.
# The script handles cases where numbers are not recognized by clicking on unprocessed (leftover) squares.

import pyautogui
import time
import numpy as np
import pytesseract
import cv2
from PIL import Image, ImageDraw
from pynput import mouse

# Screen region coordinates for capturing
px, py, rx, ry = 1075, 234, 1804, 693
level = 4

def get_pics():
    """Capture and process screenshots to identify and click on numbered squares."""
    time.sleep(0.1)
    locations, leftovers = {}, {}
    pic_large = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
    pic_large_pil = pic_large.copy()
    positions_rel = get_grid_square_positions_rel()
    
    for pos in positions_rel:
        found, x, y = False, int(pos[0]), int(pos[1])
        pic_large_np = np.array(pic_large)

        for i in range(40):
            x_offset, y_offset = x + i - 20, y + i - 20
            pixel = pic_large_np[y_offset, x_offset]
            if not np.array_equal(pixel[:3], (71, 133, 203)):
                found = True
                break

        if found:
            process_and_click_number(px + x - 35, py + y - 33, locations, leftovers)

    click_remaining_numbers(locations, leftovers)
    prepare_for_next_level()

def process_and_click_number(x, y, locations, leftovers):
    """Process individual square for number identification and handle clicking."""
    pic = pyautogui.screenshot(region=(x, y, 75, 73))
    pic = preprocess_image_for_ocr(pic)
    text = pytesseract.image_to_string(pic, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789').strip()

    if text == "":
        text = pytesseract.image_to_string(pic, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789').strip()

  
    try:       
        if text == "":
            leftovers[len(leftovers)] = ((x, y))
        key = int(text)  # Assuming the keys are integers
        if key in locations:
            if key == 3:
                locations[8] = (x, y)
            if key == 8:
                locations[3] = (x, y)
            if key == 6:
                locations[9] = (x, y)
            if key == 9:
                locations[6] = (x, y)
        if key == 6 and 6 in locations:
            locations[9] = (x, y)
        if key == 9 and 9 in locations:
            locations[6] = (x, y)
        else:
            locations[key] = (x, y)
    except ValueError:
        print("found invalid key")

def preprocess_image_for_ocr(image):
    """Preprocess the image to enhance OCR accuracy."""
    width, height = image.size
    image = image.crop((width * 0.10, height * 0.15, width * 0.90, height * 0.85))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    return cv2.threshold(image, 0, 255, cv2.THRESH_TOZERO)[1]

def click_remaining_numbers(locations, leftovers):
    """Click on the remaining numbers based on the identified sequence."""
    global level
    leftovers_index = 0
    for i in range(1, level + 1):
        if i in locations:
            pyautogui.click(locations[i][0] + 40, locations[i][1] + 40)
            time.sleep(0.1)
        elif leftovers_index in leftovers:
            pyautogui.click(leftovers[leftovers_index][0] + 40, leftovers[leftovers_index][1] + 40)
            leftovers_index += 1
            time.sleep(0.1)

def prepare_for_next_level():
    """Prepare for the next level in the sequence."""
    global level
    time.sleep(0.1 if level % 5 else 5)
    pyautogui.click(1433, 610)
    level += 1

def get_grid_square_positions_rel():
    """Calculate relative positions of squares in the grid."""
    square_width = (rx - px) / 8
    square_height = (ry - py) / 5
    return [(col * square_width + square_width / 2, row * square_height + square_height / 2) for row in range(5) for col in range(8)]

def on_click(x, y, button, pressed):
    """Handle mouse click events."""
    if pressed:
        while True:
            get_pics()

# Set up a listener for mouse click
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

import pyautogui
from pynput import mouse
import time
import numpy as np
import pytesseract
import math
import cv2
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import pandas
import keyboard

level = 4
px = 1075
py = 234
rx = 1804
ry = 693

def getPics():
    time.sleep(0.1)
    locations = {}
    leftovers = {}
    x = px
    y = py
    global level
    posish = 0
    index = 1
    picLarge = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
    picLargePIL = picLarge.copy()
    positions = get_grid_square_positions()
    positionsRelative = get_grid_square_positions_rel()
    for pos in positionsRelative:
        found = False
        for i in range(40):
            x, y = int(pos[0] + i -20), int(pos[1] + i -20)
            
            picLarge = np.array(picLarge)
            pixel = picLarge[y, x]
            target_color = (71, 133, 203)
            if (pixel[0], pixel[1], pixel[2]) != target_color:
                found = True
                break
        if found:
            draw = ImageDraw.Draw(picLargePIL) 
  
            # Drawing a green rectangle 
            # in the middle of the image 
            draw.rectangle(xy = (x, y, x+ 40, y +40), 
                        fill = (0, 127, 0), 
                        outline = (255, 255, 255), 
                        width = 5) 
            x, y = int(pos[0]) - 39, int(pos[1] - 39)
            pic = pyautogui.screenshot(region=(px + x + 4, py + y + 6, 75, 73))
            
            width, height = pic.size

            crop_width = width * 0.10
            crop_height = height * 0.15

            # Crop the image
            
            pic = pic.crop((crop_width, crop_height, width - crop_width, height - crop_height))
            pic = np.array(pic)
            pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
            pic = cv2.threshold(pic,0,255,cv2.THRESH_TOZERO)[1]
            text = pytesseract.image_to_string(pic, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789 -c page_separator=""').strip()
            if text == "":
                
                text = pytesseract.image_to_string(pic, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789 -c page_separator=""').strip()
            pic = Image.fromarray(pic)
            index += 1
            
            
    
    leftoversIndex = 0
    for i in range(1, level + 1):
        if i in locations:
            pyautogui.click(locations[i][0] + 40, locations[i][1] + 40)
            time.sleep(0.1)
        elif leftoversIndex in leftovers:
            pyautogui.click(leftovers[leftoversIndex][0] + 40, leftovers[leftoversIndex][1] + 40)
            leftoversIndex += 1
            time.sleep(0.1)
    time.sleep(0.1)
    level += 1
    if level % 5 == 0:
        time.sleep(5)
    pyautogui.click(1433, 610)


def get_grid_square_positions():
    square_width = (rx - px) / 8
    square_height = (ry - py) / 5
    positions = []
    for row in range(5):
        for col in range(8):
            x = px + (col * square_width) + (square_width / 2)
            y = py + (row * square_height) + (square_height / 2)
            positions.append((x, y))
    return positions

def get_grid_square_positions_rel():
    square_width = (rx - px) / 8
    square_height = (ry - py) / 5
    positions = []
    for row in range(5):
        for col in range(8):
            x = (col * square_width) + (square_width / 2)
            y = (row * square_height) + (square_height / 2)
            positions.append((x, y))
    return positions

def on_click(x, y, button, pressed):
    if pressed:
        while True:
                getPics()
            

# Set up a listener for mouse click
with mouse.Listener(on_click=on_click) as listener:
    listener.join()


