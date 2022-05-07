import sys

num_count = int(input())

value = 0
max_diff = - sys.maxsize
is_equal = False
for i in range(num_count):
    first_number = float(input())
    second_number = float(input())
    sum_numbers = first_number + second_number
    if i == 0:
        value = sum_numbers
    else:
        if value != sum_numbers:
            max_diff = abs(value - sum_numbers)
            value = sum_numbers
            is_equal = True
if not is_equal == True:
    print(f"Yes, value={value:.0f}")
else:
    print(f"No, maxdiff={max_diff:.0f}")
# print(value, max_diff)
