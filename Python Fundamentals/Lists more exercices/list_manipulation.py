numbers = input().split(' ')
copy_numbers = list(map(int, numbers))
even_list = []
odd_list = []
list_for_counters = []
for i in range(len(copy_numbers)):
    if copy_numbers[i] % 2 == 0:
        even_list.append(copy_numbers[i])
    else:
        odd_list.append(copy_numbers[i])
command = input()
while command != 'end':
    command_list = command.split(' ')
    list_for_counters = []
    if command_list[0] == 'exchange':
        if 0 <= int(command_list[-1]) <= len(copy_numbers)-1:
            listA = copy_numbers[:int(command_list[-1]) + 1]
            listB = copy_numbers[int(command_list[-1]) + 1:]
            copy_numbers = listB + listA
            even_list = []
            odd_list = []
            for i in range(len(copy_numbers)):
                if copy_numbers[i] % 2 == 0:
                    even_list.append(copy_numbers[i])
                else:
                    odd_list.append(copy_numbers[i])
        else:
            print("Invalid index")

    if command_list[0] == 'max':
        if command_list[-1] == 'even':
            if len(even_list) != 0:
                max_value = max(even_list)
                if even_list.count(max_value) > 1:
                    copy_numbers.reverse()
                    index = len(copy_numbers) - 1 - copy_numbers.index(max_value)
                    copy_numbers.reverse()
                else:
                    index = copy_numbers.index(max_value)
                print(index)
            else:
                print("No matches")
        elif command_list[-1] == 'odd':
            if len(odd_list) != 0:
                max_value = max(odd_list)
                if odd_list.count(max_value) > 1:
                    copy_numbers.reverse()
                    index = len(copy_numbers) - 1 - copy_numbers.index(max_value)
                    copy_numbers.reverse()
                else:
                    index = copy_numbers.index(max_value)
                print(index)
            else:
                print("No matches")

    elif command_list[0] == 'min':
        if command_list[-1] == 'even':
            if len(even_list) != 0:
                min_value = min(even_list)
                if even_list.count(min_value) > 1:
                    copy_numbers.reverse()
                    index = len(copy_numbers) - 1 - copy_numbers.index(min_value)
                    copy_numbers.reverse()
                else:
                    index = copy_numbers.index(min_value)
                print(index)
            else:
                print("No matches")
        elif command_list[-1] == 'odd':
            if len(odd_list) != 0:
                min_value = min(odd_list)
                if odd_list.count(min_value) > 1:
                    copy_numbers.reverse()
                    index = len(copy_numbers) - 1 - copy_numbers.index(min_value)
                    copy_numbers.reverse()
                else:
                    index = copy_numbers.index(min_value)
                print(index)
            else:
                print("No matches")

    elif command_list[0] == 'first':
        if command_list[-1] == 'even':
            if int(command_list[1]) > len(copy_numbers):
                print("Invalid count")
            else:
                for i in range(len(copy_numbers)):
                    if int(copy_numbers[i]) % 2 == 0:
                        if len(list_for_counters) != int(command_list[1]):
                            list_for_counters.append(copy_numbers[i])
                print(list_for_counters)

        elif command_list[-1] == 'odd':
            if int(command_list[1]) > len(copy_numbers):
                print("Invalid count")
            else:
                for i in range(len(copy_numbers)):
                    if int(copy_numbers[i]) % 2 != 0:
                        if len(list_for_counters) != int(command_list[1]):
                            list_for_counters.append(copy_numbers[i])
                print(list_for_counters)

    elif command_list[0] == 'last':

        if command_list[-1] == 'even':
            if int(command_list[1]) > len(copy_numbers):
                print("Invalid count")
            else:
                copy_numbers.reverse()
                for i in range(len(copy_numbers)):
                    if int(copy_numbers[i]) % 2 == 0:
                        if len(list_for_counters) != int(command_list[1]):
                            list_for_counters.append(copy_numbers[i])
                list_for_counters.reverse()
                copy_numbers.reverse()
                print(list_for_counters)

        if command_list[-1] == 'odd':
            if int(command_list[1]) > len(copy_numbers):
                print("Invalid count")
            else:
                copy_numbers.reverse()
                for i in range(len(copy_numbers)):
                    if int(copy_numbers[i]) % 2 != 0:
                        if len(list_for_counters) != int(command_list[1]):
                            list_for_counters.append(copy_numbers[i])
                list_for_counters.reverse()
                copy_numbers.reverse()
                print(list_for_counters)

    command = input()
print(copy_numbers)
