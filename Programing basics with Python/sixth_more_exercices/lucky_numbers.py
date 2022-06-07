N = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        sum1 = num1 + num2
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                sum2 = num3 + num4
                if sum1 == sum2:
                    if N % sum1 == 0:
                        print(f'{num1}{num2}{num3}{num4}', end=' ')
