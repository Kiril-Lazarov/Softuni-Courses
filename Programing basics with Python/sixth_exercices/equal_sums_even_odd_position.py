first_number = int(input())
second_number = int(input())

isEqual = False
for number in range(first_number, second_number + 1):
    str_number = str(number)
    odd_sum = 0
    even_sum = 0
    for i, digit in enumerate(str_number):
        dig = int(digit)
        if (i+1) % 2 == 1:
            odd_sum += dig
        else:
            even_sum += dig
    if even_sum == odd_sum:
        print(number, end=' ')


