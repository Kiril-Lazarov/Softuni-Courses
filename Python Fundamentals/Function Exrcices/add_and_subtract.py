def sum_numbers(a, b):
    return a + b


def subtract(c):
    return sum_numbers(num1, num2) - c


def add_and_subtract(a, b, c):
    return sum_numbers(a, b) - subtract(c)



num1, num2, num3 = int(input()), int(input()), int(input())





print(subtract(num3))
