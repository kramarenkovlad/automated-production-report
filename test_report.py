from openpyxl import load_workbook

workbook = load_workbook("summary.xlsx")
sheet = workbook["Production Summary"]

assert sheet["B2"].value == 600
assert sheet["B3"].value == 25
assert sheet["B4"].value == 575
assert sheet["B5"].value == 4.17
assert sheet["A1"].font.bold == True
assert sheet.column_dimensions["A"].width == 25

print("ALL TESTS PASSED")

