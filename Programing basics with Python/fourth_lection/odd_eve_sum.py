count_number = int(input())
odd_sum = 0
even_sum = 0
for position in range(1, count_number + 1):
    current_number = int(input())
    if position % 2 == 1:
        odd_sum += current_number
    else:
        even_sum += current_number
if odd_sum == even_sum:
    print('Yes')
    print(f'{"Sum ="} { odd_sum}')
else:
    print('No')
    print(f'{"Diff = "}{abs(odd_sum - even_sum)}')
