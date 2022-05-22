judge_num = int(input())
presentation_name = input()
total_grade = 0
counter_presentations = 0
while presentation_name != 'Finish':
    grades_sum = 0
    counter_grades = 0
    while counter_grades != judge_num:
        grade = float(input())
        grades_sum += grade
        counter_grades += 1
    total_grade += grades_sum
    counter_presentations += judge_num
    print(f"{presentation_name} - {grades_sum / counter_grades:.2f}.")
    presentation_name = input()
print(f"Student's final assessment is {total_grade / counter_presentations:.2f}.")
