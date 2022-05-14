start = int(input())
final = int(input())
magic_number = int(input())
counter_number = 0
isFound = False
for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        counter_number += 1
        if first_number + second_number == magic_number:
            isFound = True
            break
    if isFound:
        break
if isFound:
    print(f"Combination N:{counter_number} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter_number} combinations - neither equals {magic_number}")
