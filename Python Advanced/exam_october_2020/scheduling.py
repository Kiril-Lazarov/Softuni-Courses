numbers = [int(x) for x in input().split(', ')]
# numbers = [int(x) for x in "3, 1, 10, 1, 2".split(', ')]
n = int(input())
total_cycles = 0
needed_number = numbers[n]
curr_value = 0
while True:
    curr_value = min(numbers)
    counter = numbers.count(curr_value)

    if  counter == 1:
        total_cycles += curr_value
        numbers.remove(curr_value)
    else:
        for _ in range(counter):
            numbers.remove(curr_value)
        total_cycles += curr_value * counter
    if numbers.count(needed_number) == 0:
        break

print(total_cycles)