# Human Benchmark Automation Scripts

**Author:** Jeronimo del Valle  
**Creation Date:** 2024-01-09  
**Last Edited:** 2024-01-09

## Overview
This repository contains a collection of Python scripts designed to automate different tests available on the Human Benchmark website (https://humanbenchmark.com/). These scripts leverage various Python libraries to interact with the user's screen, analyze visual data, and automate mouse and keyboard actions. 

## Description
The scripts in this repository automate tasks ranging from clicking on white squares to reading text using OCR (Optical Character Recognition) and performing automated actions based on the content. Each script is tailored to a specific test or action on the Human Benchmark website, providing a unique approach to automation. The common libraries used across these scripts include `pyautogui`, `pynput`, `numpy`, `pytesseract`, and `cv2`.

### Key Features:
1. **Click Automation:** Scripts to identify and automate clicks on white squares, colored pixels, and numbered squares within a specific screen region.
2. **OCR-Based Actions:** Utilizes `pytesseract` to read text and numbers from the screen and perform automated clicks and keyboard actions.
3. **Dynamic Area Processing:** Expands the search area dynamically with each iteration for improved efficiency.
4. **Image Recognition:** Finds specified target images on the screen and clicks at their center.
5. **Text Extraction and Typing:** Captures a screenshot of a user-defined screen region, extracts text using OCR, and types out the processed text.

## Usage
These scripts are designed to be straightforward and user-friendly. Users can define regions on their screen, automate clicks, and process screen data without manual intervention. The repository provides clear documentation for each script, outlining its purpose and usage instructions.

## Requirements
- Python 3.x
- Libraries: `pyautogui`, `pynput`, `numpy`, `pytesseract`, `cv2`, `PIL`
- Tesseract OCR Engine

## Disclaimer
This project is for educational purposes only. Users should abide by the Human Benchmark website's terms of service when using these scripts.

## Contributions
Contributions to this repository are welcome. Please ensure that any contributions adhere to the existing code structure and documentation standards.

---

## Demo Videos

Here are some demo videos showcasing the functionalities of these scripts:

- **Visual Memory**
  ![Memory Squares](img/vidGif/MemorySquares.gif)

- **Chimp Test**
  ![Monkey](img/vidGif/Monkey.gif)

- **Number Memory**
  ![Number Memory](img/vidGif/NumberMemory.gif)

- **Reaction Time**
  ![Reaction](img/vidGif/Reaction.gif)

- **Sequence Memory**
  ![Sequence](img/vidGif/Sequence.gif)

- **Aim Trainer**
  ![Targets](img/vidGif/Targets.gif)

- **Typing**
  ![Typing](img/vidGif/Typing.gif)

- **Verbal Memory**
  ![Word Memory](img/vidGif/WordMemory.gif)

