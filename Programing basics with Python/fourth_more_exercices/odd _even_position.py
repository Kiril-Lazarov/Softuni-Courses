import sys

num_count = int(input())
odd_numbers = 0
even_numbers = 0
min_odd = sys.maxsize
max_odd = -sys.maxsize
min_even = sys.maxsize
max_even = -sys.maxsize
even_count = 0
odd_count = 0
for i in range(1, num_count + 1):
    number = float(input())
    if i % 2 == 1:
        odd_numbers += number
        odd_count += 1
        if number > max_odd:
            max_odd = number
        if number < min_odd:
            min_odd = number
    else:
        even_numbers += number
        even_count += 1
        if number > max_even:
            max_even = number
        if number < min_even:
            min_even = number

print(f"OddSum={odd_numbers:.2f},")
if odd_count != 0:
    print(f"OddMin={min_odd:.2f},")
    print(f"OddMax={max_odd:.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")

print(f"EvenSum={even_numbers:.2f},")
if even_count != 0:
    print(f"EvenMin={min_even:.2f},")
    print(f"EvenMax={max_even:.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
