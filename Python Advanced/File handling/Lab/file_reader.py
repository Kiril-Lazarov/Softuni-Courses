file = open('./number.txt', 'r')
count= 0
for number in file:
    count += int(number)
print(count)