# CGPA Calculator by msladan01 - 200L
print("=== CGPA Calculator ===")
total_units = 0
total_points = 0
num = int(input("How many courses? "))

for i in range(num):
    unit = int(input(f"Unit for course {i+1}: "))
    grade = input("Grade (A/B/C/D/E/F): ").upper()
    if grade == "A": point = 5
    elif grade == "B": point = 4
    elif grade == "C": point = 3
    elif grade == "D": point = 2
    elif grade == "E": point = 1
    else: point = 0
    total_units += unit
    total_points += unit * point

cgpa = total_points / total_units
print(f"Your CGPA is: {cgpa:.2f}")
