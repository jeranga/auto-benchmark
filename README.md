# auto-benchmark
Automate Human Benchmark tests with Python scripts. Features include click automation, OCR-based actions, dynamic area processing, image recognition, and text extraction. Ideal for educational purposes.
Overview
This repository contains a collection of Python scripts designed to automate different tests available on the Human Benchmark website (https://humanbenchmark.com/). These scripts leverage various Python libraries to interact with the user's screen, analyze visual data, and automate mouse and keyboard actions.

Description
The scripts in this repository automate tasks ranging from clicking on white squares to reading text using OCR (Optical Character Recognition) and performing automated actions based on the content. Each script is tailored to a specific test or action on the Human Benchmark website, providing a unique approach to automation. The common libraries used across these scripts include pyautogui, pynput, numpy, pytesseract, and cv2.

Key Features:
Click Automation: Scripts to identify and automate clicks on white squares, colored pixels, and numbered squares within a specific screen region.
OCR-Based Actions: Utilizes pytesseract to read text and numbers from the screen and perform automated clicks and keyboard actions.
Dynamic Area Processing: Expands the search area dynamically with each iteration for improved efficiency.
Image Recognition: Finds specified target images on the screen and clicks at their center.
Text Extraction and Typing: Captures a screenshot of a user-defined screen region, extracts text using OCR, and types out the processed text.
Usage
These scripts are designed to be straightforward and user-friendly. Users can define regions on their screen, automate clicks, and process screen data without manual intervention. The repository provides clear documentation for each script, outlining its purpose and usage instructions.

Requirements
Python 3.x
Libraries: pyautogui, pynput, numpy, pytesseract, cv2, PIL
Tesseract OCR Engine
Disclaimer
This project is for educational purposes only. Users should abide by the Human Benchmark website's terms of service when using these scripts.

Contributions
Contributions to this repository are welcome. Please ensure that any contributions adhere to the existing code structure and documentation standards.
