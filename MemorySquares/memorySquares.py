# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script automates the process of clicking on white squares within a specified region of the screen.
# It takes a screenshot of a selected region, identifies columns of light blue, and performs clicks on white squares.
# The script is useful for automating repetitive clicking tasks in applications where white squares appear in a grid layout.

from pynput import mouse
import pyautogui
import time
import numpy as np

# Coordinates for the region of interest on the screen
px, py, rx, ry = 1248, 309, 1626, 685

def click(x, y):
    """Simulate a mouse click at the specified coordinates."""
    time.sleep(1)
    pyautogui.moveTo(x, y)
    pyautogui.click()

def is_light_blue(pixel):
    """Check if the pixel color matches light blue."""
    target_color = (71, 133, 203)
    return np.array_equal(pixel[:3], target_color)


def is_white(pixel):
    """Check if the pixel color is white."""
    threshold = 200  
    return all(component >= threshold for component in pixel[:3])

def get_cols():
    """Capture a screenshot and count the number of columns in the grid."""
    pic = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
    img = np.array(pic)
    gap_count, in_gap = 0, False
    for y in range(ry - py):
        pixel = img[y, 5]
        if is_light_blue(pixel):
            if not in_gap:
                in_gap, gap_count = True, gap_count + 1
        elif in_gap:
            in_gap = False
    return gap_count + 1, img

def get_grid_square_positions(columns):
    """Calculate the positions of squares in the grid."""
    square_width, square_height = (rx - px) / columns, (ry - py) / columns
    return [(px + col * square_width + square_width / 2, py + row * square_height + square_height / 2) 
            for row in range(columns) for col in range(columns)]

def click_white_squares(columns, img):
    """Click on white squares in the grid."""
    positions = get_grid_square_positions(columns)
    for pos in positions:
        x, y = map(int, pos)
        pixel = img[y - py, x - px]
        if is_white(pixel):
            pyautogui.click(x, y)
            time.sleep(0.1)

def on_click(x, y, button, pressed):
    """Handle mouse click events to start the automation process."""
    if pressed:
        time.sleep(1)
        print("Starting automation...")
        while True:
            columns, img = get_cols()
            time.sleep(1)
            click_white_squares(columns, img)
            time.sleep(2)

# Set up a listener for mouse clicks to initiate the process
with mouse.Listener(on_click=on_click) as listener:
    listener.join()