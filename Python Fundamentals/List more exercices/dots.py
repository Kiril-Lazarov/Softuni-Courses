from math import factorial
n = int(input())
points = 0
dots_list = list()
current = []
dots_indexes_list = []
for i in range(n):
    a = input().split(' ')
    dots_list.append(a)
for j in range(len(dots_list)):
    for k in range(len(dots_list[j])):
        if dots_list[j][k] == '.':
            dots_indexes_list.append([j, k])
for i in range(factorial(len(dots_indexes_list))):
    for j in range(2):
        if dots_indexes_list[i][0] == dots_indexes_list[i+1][0] or dots_indexes_list[i][1] == dots_indexes_list[i+1][1]:
            points +=1
print(dots_indexes_list)
print(points)






