# Student Grade Analyzer - Automated Academic Reporting System

A Python-based automation tool that streamlines student performance analysis and report card generation.

## Overview
This system automates the manual process of calculating student results, reducing analysis time from hours to seconds for 100+ records.

## Key Features
- **Automated Calculation:** Computes Total, Average, Result (Pass/Fail) and Grade (A/B/C/F)
- **Top Performer Detection:** Uses `idxmax()` to identify topper with highest total
- **Result Analytics:** Generates Pass/Fail distribution using `value_counts()`
- **Grade Classification:** Smart grading logic (A: >=85, B: >=60, C: >=35, F: <35)
- **Visual Report Cards:** Auto-generates printable PNG report cards for each student
- **Class Insights:** Calculates overall class average and performance summary

## Tech Stack
- Python 3.x
- Pandas - Data manipulation and analysis
- Pillow (PIL) - Report card image generation

## Code Logic
1. Creates DataFrame from student records
2. Performs row-wise aggregation for Total Marks
3. Applies lambda functions for Result and Grade evaluation
4. Generates individual report cards with color-coded grades

## Output
- Formatted marksheet table
- Class average and topper details
- Result and grade distribution
- `/cards` folder with individual report cards

## How to Run
```bash
pip install pandas pillow
python card.py