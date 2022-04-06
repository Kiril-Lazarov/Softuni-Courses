number = int(input())
number_count = 0
sum_number = 0

while True:
    input_number = int(input())
    number_count += 1
    sum_number += input_number
    if number_count < number:
        continue
    else:
        break

print(f'{sum_number / number:.2f}')
