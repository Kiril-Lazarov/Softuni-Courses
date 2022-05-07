# 1.	Капацитетът на стадиона – цяло число в интервала [1 … 10000];
# 2.	Броят на всички фенове – цяло число в интервала [1 … 10000].
# 1.	Процентът на феновете в сектор А
# 2.	Процентът на феновете в сектор Б
# 3.	Процентът на феновете в сектор В
# 4.	Процентът на феновете в сектор Г
# 5.	Процентът на всички фенове, спрямо капацитета на стадиона.

stadium_capacity = int(input())
fan_count = int(input())

groupA = 0
groupB = 0
groupV = 0
groupG = 0

for i in range(fan_count):
    stadium = input()
    if stadium == 'A':
        groupA += 1
    elif stadium == 'B':
        groupB += 1
    elif stadium == 'V':
        groupV += 1
    else:
        groupG += 1
print(f'{groupA / fan_count * 100:.2f}%')
print(f'{groupB / fan_count * 100:.2f}%')
print(f'{groupV / fan_count * 100:.2f}%')
print(f'{groupG / fan_count * 100:.2f}%')
print(f'{fan_count / stadium_capacity *100:.2f}%')
