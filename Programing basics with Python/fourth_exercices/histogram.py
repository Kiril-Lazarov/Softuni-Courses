count_numbers = int(input())

first_range_numbers = 0
second_range_numbers = 0
third_range_numbers = 0
fourth_range_numbers = 0
fifth_range_numbers = 0

for number in range(1, count_numbers + 1):
    current_number = int(input())
    if current_number < 200:
        first_range_numbers += 1
    if 200 <= current_number <= 399:
        second_range_numbers += 1
    if 400 <= current_number <= 599:
        third_range_numbers += 1
    if 600 <= current_number <= 799:
        fourth_range_numbers += 1
    if 800 <= current_number <= 1000:
        fifth_range_numbers += 1
print(f'{first_range_numbers / count_numbers * 100:.2f}%')
print(f'{second_range_numbers / count_numbers * 100:.2f}%')
print(f'{third_range_numbers / count_numbers * 100:.2f}%')
print(f'{fourth_range_numbers / count_numbers * 100:.2f}%')
print(f'{fifth_range_numbers / count_numbers * 100:.2f}%')