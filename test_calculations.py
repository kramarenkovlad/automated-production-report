from report import calculate_summary

shifts = [
    {"name": "Morning", "total": 500, "defective": 20},
    {"name": "Evening", "total": 100, "defective": 5}
]

result = calculate_summary(shifts)

assert result["total"] == 600
assert result["defective"] == 25
assert result["good"] == 575
assert round(result["defect_rate"], 2) == 4.17

print("TEST 1 PASSED")

shifts = []

result = calculate_summary(shifts)

assert result["total"] == 0
assert result["defective"] == 0
assert result["good"] == 0
assert round(result["defect_rate"], 2) == 0

print("TEST 2 PASSED")

shifts = [
    {"name": "Morning", "total": 100, "defective": 100}
]

result = calculate_summary(shifts)

assert result["total"] == 100
assert result["good"] == 0
assert round(result["defect_rate"], 2) == 100

print("TEST 3 PASSED")