count_numbers = int(input())
left_sum = 0
right_sum = 0

# for numbers in range(1, (2 * count_numbers) + 1):

for left_numbers in range(1, count_numbers + 1):
    current_number = int(input())
    left_sum += current_number
for right_numbers in range((count_numbers + 1), (2 * count_numbers) + 1):
    current_number = int(input())
    right_sum += current_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")

