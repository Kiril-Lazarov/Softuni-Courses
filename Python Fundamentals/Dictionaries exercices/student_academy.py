def average(data_grades_dict):
    for key, value in data_grades_dict.items():
        average_grade = sum(value) / len(value)
        if average_grade >= 4.5:
            print(f'{key} -> {average_grade:.2f}')

def student_academy():
    data_grades_dict = {}
    number = int(input())
    for data in range(number):
        name = input()
        grade = float(input())
        if name not in data_grades_dict:
            data_grades_dict[name] = []
        data_grades_dict[name].append(grade)
    average(data_grades_dict)
student_academy()