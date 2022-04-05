failed_grades_count = int(input())
task_name = input()
unsatisfied_grade_count = 0
task_number = 0
average_grade = 0
last_task = ""
is_equal = False
while task_name != "Enough":
    grade = int(input())
    last_task = task_name
    task_number += 1
    average_grade += grade
    if grade <= 4:
        unsatisfied_grade_count += 1
    if unsatisfied_grade_count == failed_grades_count:
        is_equal = True
        break
    task_name = input()
if is_equal != is_equal:
    print(f"You need a break, {unsatisfied_grade_count} poor grades.")
else:
    print(f"Average score: {average_grade / task_number:.2f}")
    print(f"Number of problems: {task_number}")
    print(f"Last problem: {last_task}")
