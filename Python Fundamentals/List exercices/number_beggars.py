integers = input()
n = int(input())
list = list()
number = ''
score = 0
final_list = []
for i in range(len(integers)):
    if integers[i] != chr(44) and integers[i] != ' ':
        number += integers[i]
    elif integers[i] == ',':
        list.append(int(number))
        number = ''
list.append(int(number))
if n == len(list):
    print(list)
elif n > len(list):
    for i in range(n -len(list)):
        list.append(0)
    print(list)
else:
    for i in range(n):
        for j in range(i, len(list), n):
            score += int(list[j])
        final_list.append(score)
        score = 0
    print(final_list)