list_num = input().split(' ')
counter_to_remove = int(input())
numbers = ''
for i in range(len(list_num)):
    list_num[i] = int(list_num[i])
for i in range(counter_to_remove):
    list_num.remove(min(list_num))
for j in range(len(list_num)):
    if j == 0:
        numbers += f'{list_num[j]}'
    else:
        numbers += f', {list_num[j]}'

print(numbers)