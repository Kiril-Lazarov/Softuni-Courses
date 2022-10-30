numbers = input().split(' ')
final_nums = []

for i in numbers:
    current_num = abs(float(i))
    final_nums.append(current_num)

print(final_nums)
