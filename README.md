# README: Working time calculator

## Description
The **Work Hours Calculator** is a Python-based GUI application designed to track and calculate work hours. It allows users to input daily work times and calculates the total hours while automatically applying break rules.

## Features
- **Daily Work Time Tracking**:  
  - Input start and end times for each workday.  
  - Automatically calculates daily work hours.
- **Break Adjustment**:  
  - For work durations over 6 hours, up to 30 minutes of break time is automatically deducted.
- **Multiple Day Support**:  
  - Add as many days as needed, with individual time calculations for each.
- **Total Time Calculation**:  
  - Sums up the work hours for all days and displays the total in hours and minutes.
- **User-Friendly Interface**:  
  - Drop-down menus for selecting time inputs.  
  - Error handling for invalid inputs.

## How to Use
1. **Launch**: Run the program by executing the script (`python work_hours_calculator.py`).
2. **Input Times**: Select start and end times for each day using the drop-down menus.
3. **Add Days**: Add additional days as needed using the provided button.
4. **Calculate Total Time**:  
   - Click on "Calculate Total Time" to compute the overall working hours.  
   - A pop-up window will display the total hours and minutes.

## System Requirements
- **Python 3.x**  
- **Tkinter Library** (included by default with Python)  
