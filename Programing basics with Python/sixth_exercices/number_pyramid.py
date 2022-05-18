number = int(input())
number1 = number
rows = 0
counter_rows = 0
counter_numbers = 0
isBigger = False
while number > 0:
    counter_rows += 1
    number -= (rows + 1)
    rows += 1
for row in range(counter_rows+1):
    for col in range(1, row + 1):
        counter_numbers += 1
        print(counter_numbers, end=' ')
        if counter_numbers == number1:
            isBigger = True
            break
    if isBigger:
        break
    print()

