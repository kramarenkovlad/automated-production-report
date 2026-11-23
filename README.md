
# Automated Production Report

## Description

A Python project for automating production reports.

The program reads production data from a CSV file,
checks for invalid values, calculates production
statistics, and generates CSV and Excel reports.

## Features

- Reads production data from CSV files
- Validates production and defect values
- Skips invalid data
- Calculates total production
- Calculates total defective products
- Calculates good products
- Calculates defect percentage
- Creates CSV and Excel reports
- Formats Excel reports

## Technologies

- Python
- CSV
- openpyxl

## How to Run

Install dependencies:

    python -m pip install -r requirements.txt

Run the program:

    python report.py

The program reads shifts_test.csv and creates
summary.csv and summary.xlsx.

## Testing

Run the main program first to generate summary.xlsx.

Then run the tests:

    python test_calculations.py
    python test_report.py

The tests check production calculations
and Excel report values.
