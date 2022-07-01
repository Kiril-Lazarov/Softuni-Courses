first_string = input()
second_string = input()
result = ''
part_first_string = ''
for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        result += second_string[i]
        for j in range(i, len(first_string) - 1):
            part_first_string += first_string[j + 1]
        print(f'{result}{part_first_string}')
        part_first_string = ''
    else:
        result += second_string[i]
