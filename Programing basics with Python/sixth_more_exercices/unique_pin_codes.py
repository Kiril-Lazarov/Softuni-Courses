# •	Горната граница на първото число - цяло число в диапазона [1...9]
# •	Горната граница на второто число - цяло число в диапазона [1...9]
# •	Горната граница на третото число - цяло число в диапазона [1...9]

first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())

num1 = 0
num2 = 0
num3 = 0

for first_num in range(1, first_num_limit + 1):
    if first_num % 2 == 0:
        num1 = first_num
        for second_num in range(2, second_num_limit + 1):
            if second_num <= 7:
                for i in range(2, 8):
                    if second_num != 4 and second_num != 6:

                        if second_num % i == 0:
                            if second_num // i == 1 or second_num // i == i:
                                num2 = second_num
                                for third_num in range(1, third_num_limit + 1):
                                    if third_num % 2 == 0:
                                        num3 = third_num
                                        print(num1, num2, num3)

            else:
                break
    num1 = 0
    num2 = 0
    num3 = 0
