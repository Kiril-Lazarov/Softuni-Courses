numbers = list(map(int, input().split(', ')))
index_list = list()
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        index_list.append(i)


print(index_list)