from math import floor

startvalue_first_pair = int(input())
startvalue_second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())

isFirstPrime = False
isSecondPrime = False

for first_pair in range(startvalue_first_pair, startvalue_first_pair + diff_first_pair + 1):
    divisor1 = 2
    isFirstPrime = False
    while first_pair % divisor1 != 0:
        if divisor1 < floor(first_pair / 2):
            divisor1 += 1
        else:
            isFirstPrime = True
            break
    for second_pair in range(startvalue_second_pair, startvalue_second_pair + diff_second_pair + 1):
        divisor2 = 2
        isSecondPrime = False
        while second_pair % divisor2 != 0:
            if divisor2 < floor(second_pair / 2):
                divisor2 += 1
            else:
                isSecondPrime = True
                break
        if isFirstPrime == True and isSecondPrime == True:
            print(f'{first_pair}{second_pair}')
