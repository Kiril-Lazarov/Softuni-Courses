N = int(input())

for number in range(1111, 10000):
    counter_digit = 0
    for digit in str(number):
        if int(digit) != 0:
            if N % int(digit) == 0:
                counter_digit += 1
    if counter_digit == 4:
        print(number, end=' ')
