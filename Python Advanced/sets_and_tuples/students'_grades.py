n = int(input())

stud_dict = {}

for _ in range(n):
    name, grade = input().split(" ")
    if name not in stud_dict:
        stud_dict[name] = []
    stud_dict[name].append(float(f"{float(grade):.2f}"))

for name, grade in stud_dict.items():
    avg = sum(stud_dict[name])/len(stud_dict[name])
    string= ''
    for grades in stud_dict[name]:
        string += f'{grades:.2f}' + ' '
    print(f'{name} -> {string}(avg: {avg:.2f})')


