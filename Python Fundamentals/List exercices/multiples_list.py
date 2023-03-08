factor = int(input())
counter = int(input())
number = 0
list1 = []
for i in range(1,counter +1):
    number = abs(factor * i )
    list1.append(number)
print(list1)