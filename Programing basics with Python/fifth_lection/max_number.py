import sys

number = input()
max_num = - sys.maxsize
while number != "Stop":
    if int(number) > max_num:
        max_num = int(number)
    number = input()
if max_num != -sys.maxsize:
    print(max_num)