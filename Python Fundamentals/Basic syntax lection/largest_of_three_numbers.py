# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
#
#
# if number1 >= number2 and number1 >= number3:
#     print(number1)
# if number2 >= number1 and number2 >= number3:
#     print(number2)
# if number3 >= number2 and number3 >= number1:
#     print(number3)

# import sys
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# n = - sys.maxsize
#
# if num1 >= n:
#     n = num1
# if num2 >= n:
#     n = num2
# if num3 >=n:
#     n = num3
# print(n)

days= { 'Mon', 'Tue', 'Wed','Thu'}
enum_days = enumerate(days)
print(type(enum_days))

# converting it to alist
print(list(enum_days))

# changing the default counter to 5
enum_days = enumerate(days, 5)
print(list(enum_days))