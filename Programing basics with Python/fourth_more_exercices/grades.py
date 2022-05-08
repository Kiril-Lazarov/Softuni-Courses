# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход

students_count = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
total_grade = 0

for i in range(students_count):
    grade = float(input())
    total_grade += grade
    if grade < 3:
        group_1 += 1
    elif grade < 4:
        group_2 += 1
    elif grade < 5:
        group_3 += 1
    else:
        group_4 += 1

print(f"Top students: {group_4 / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {group_3 / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {group_2/ students_count * 100:.2f}%")
print(f"Fail: {group_1 / students_count * 100:.2f}%")
print(f"Average: {total_grade / students_count:.2f}")