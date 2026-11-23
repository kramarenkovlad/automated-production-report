
import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill


# 1. Read and validate CSV data
def load_shifts(filename):
    valid_shifts = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                name = row["name"]
                total = int(row["total"])
                defective = int(row["defective"])

            except (ValueError, KeyError, TypeError):
                print("ERROR: Invalid number or missing column")
                continue

            if total < 0 or defective < 0 or defective > total:
                print("ERROR: Invalid production data")
                continue

            shift = {
                "name": name,
                "total": total,
                "defective": defective
            }

            valid_shifts.append(shift)

    return valid_shifts


# 2. Calculate production summary
def calculate_summary(shifts):
    total_all = 0
    defective_all = 0

    for shift in shifts:
        total_all += shift["total"]
        defective_all += shift["defective"]

    good_all = total_all - defective_all

    if total_all == 0:
        defect_rate = 0
    else:
        defect_rate = defective_all / total_all * 100

    return {
        "total": total_all,
        "defective": defective_all,
        "good": good_all,
        "defect_rate": defect_rate
    }


# 3. Print summary to console
def print_report(summary):
    print("=== PRODUCTION SUMMARY ===")
    print("Total produced:", summary["total"])
    print("Total defective:", summary["defective"])
    print("Good products:", summary["good"])
    print("Defect rate:", round(summary["defect_rate"], 2), "%")


# 4. Save summary as CSV
def save_report_csv(summary, filename):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Total",
            "Defective",
            "Good",
            "Defect rate (%)"
        ])

        writer.writerow([
            summary["total"],
            summary["defective"],
            summary["good"],
            round(summary["defect_rate"], 2)
        ])


# 5. Save formatted Excel report
def save_report_excel(summary, filename):
    workbook = Workbook()
    sheet = workbook.active

    sheet.title = "Production Summary"

    sheet.append(["Metric", "Value"])
    sheet.append(["Total produced", summary["total"]])
    sheet.append(["Total defective", summary["defective"]])
    sheet.append(["Good products", summary["good"]])
    sheet.append([
        "Defect rate (%)",
        round(summary["defect_rate"], 2)
    ])

    # Format headers
    for cell in sheet[1]:
        cell.font = Font(
            bold=True,
            color="FFFFFF"
        )

        cell.fill = PatternFill(
            fill_type="solid",
            fgColor="1F4E78"
        )

    # Set column widths
    sheet.column_dimensions["A"].width = 25
    sheet.column_dimensions["B"].width = 18

    # Format percentage display
    sheet["B5"].number_format = '0.00"%"'

    # Save workbook
    workbook.save(filename)


# 6. Main program
if __name__ == "__main__":
    shifts = load_shifts("shifts_test.csv")

    summary = calculate_summary(shifts)

    print_report(summary)

    save_report_csv(summary, "summary.csv")
    save_report_excel(summary, "summary.xlsx")

    print("Reports saved successfully!")
