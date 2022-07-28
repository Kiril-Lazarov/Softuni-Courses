number = int(input()) +1

while True:
    num_string = str(number)

    set_num = set(num_string)
    if len(set_num) == len(num_string):
        break
    else:
        number +=1

print(number)
