student_name = input()
sum_grade = 0
year = 1
bad_grade = 0

while year <= 12 and bad_grade < 2:
    grade = float(input())
    sum_grade += grade
    if grade < 4:
        bad_grade += 1
        year -= 1
        sum_grade -= grade
    year += 1
if year > 12:
    print(f"{student_name} graduated. Average grade: {sum_grade / 12:.2f}")
else:
    print(f"{student_name} has been excluded at {year} grade")
