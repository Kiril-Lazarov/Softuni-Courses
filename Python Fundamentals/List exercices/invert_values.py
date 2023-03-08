string = input()
number = ''
list = []
for i in range(len(string)):
    if string[i] != ' ':
        number += string[i]
    else:
        number = int(number) * -1
        list.append(number)
        number = ''
number = int(number) * -1
list.append(number)
print(list)













