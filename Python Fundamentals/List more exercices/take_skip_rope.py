string_list = list(input())
numbers_list = [i for i in string_list if 48 <= ord(i) <= 57]
numbers_list = list(map(int, numbers_list))
string_list = [i for i in string_list if not 48 <= ord(i) <= 57]
take_list = []
skip_list = []
final_result = []
help_list = []
for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

for j in range(len(take_list)):
    if take_list[j] != 0:
        help_list = string_list[:take_list[j]]
        final_result += help_list
        string_list = string_list[take_list[j]:]
    if skip_list[j] != 0:
        string_list = string_list[skip_list[j]:]

print(''.join(final_result))

