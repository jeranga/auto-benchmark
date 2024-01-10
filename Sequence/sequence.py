# Author: Jeronimo del Valle
# Date of Creation: 2024-01-09
# Last Edited: 2024-01-09
#
# Description:
# This script automates the process of identifying and clicking on white squares within a specified screen region.
# It dynamically expands its search area with each iteration. The script is triggered by a mouse click and 
# uses screen capturing and pixel color analysis to locate and click the white squares.

import pyautogui
from pynput import mouse
import time
import numpy as np

# Coordinates for the region of interest on the screen
px, py, rx, ry = 1248, 309, 1626, 685

def is_white(pixel):
    """Check if the pixel color is white based on a threshold."""
    threshold = 200  
    return all(component >= threshold for component in pixel[:3])

def get_grid_square_positions(columns=3):
    """Calculate the positions of squares in a grid of specified column count."""
    square_width = (rx - px) / columns
    square_height = (ry - py) / columns
    return [(px + col * square_width + square_width / 2, py + row * square_height + square_height / 2)
            for row in range(columns) for col in range(columns)]

def get_moves(img, curr_seq):
    """Identify white squares in the image and append their positions to the current sequence."""
    positions = get_grid_square_positions()
    for pos in positions:
        x, y = map(int, pos)
        pixel = img[y - py, x - px]  # Adjust for the relative position in the image
        if is_white(pixel):
            curr_seq.append((x, y))

def on_click(x, y, button, pressed):
    """Handle mouse click events to start the automation process."""
    if pressed:
        size = 1
        while True:
            curr_seq = []
            time.sleep(1)
            for i in range(size):
                tic = time.perf_counter()
                pic = pyautogui.screenshot(region=(px, py, rx - px, ry - py))
                img = np.array(pic)
                get_moves(img, curr_seq)
                toc = time.perf_counter()
                time.sleep(max(0, 0.5 - (toc - tic)))
            time.sleep(1)
            for pos in curr_seq:
                pyautogui.click(*map(int, pos))
            size += 1

# Set up a listener for mouse clicks to initiate the process
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
