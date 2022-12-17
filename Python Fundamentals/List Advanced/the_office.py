employees_happiness = list(map(int, input().split(' ')))
number = int(input())

average_happiness = sum(employees_happiness)/len(employees_happiness)

number_happy_employees = [i for i in employees_happiness if average_happiness< i ]
if len(number_happy_employees) >= len(employees_happiness)/2:
    print(f"Score: {len(number_happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(number_happy_employees)}/{len(employees_happiness)}. Employees are not happy!")

