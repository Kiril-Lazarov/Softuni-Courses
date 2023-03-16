# first_row = input()
# second_row = input()
# third_row = input()
# line1 = []
# line2 = []
# line3 = []
# diagonal1 = []
# diagonal2 = []
# column1 = []
# column2 = []
# column3 = []
# num_ones = 0
# num_two = 0
# sum_rows = 0
# isWinner= False
# for i in range(len(first_row)):
#     if first_row[i] != ' ':
#         line1.append(int(first_row[i]))
#
# for j in range(len(second_row)):
#     if first_row[j] != ' ':
#         line2.append(int(second_row[j]))
#
# for k in range(len(third_row)):
#     if first_row[k] != ' ':
#         line3.append(int(third_row[k]))
#
# column1 = [line1[0], line2[0], line3[0]]
# column2 = [line1[1], line2[1], line3[1]]
# column3 = [line1[2], line2[2], line3[2]]
# diagonal1 = [line1[0], line2[1], line3[2]]
# diagonal2 = [line1[2], line2[1], line3[0]]
#
# for i in range(1,3):
#     final = []
#     final.append(line1.count(i))
#     final.append(line2.count(i))
#     final.append(line3.count(i))
#     final.append(column1.count(i))
#     final.append(column2.count(i))
#     final.append(column3.count(i))
#     final.append(diagonal1.count(i))
#     final.append(diagonal2.count(i))
#
#     if i == 1 and (3 in final):
#         print("First player won")
#         isWinner = True
#         break
#     elif i == 2 and (3 in final):
#         isWinner = True
#         print("Second player won")
#         break
# if isWinner == False:
#     print("Draw!")

nums = (input()).split(' ')
command = input()
list_index = []
max_v = 'max'
min_v = 'min'
even = []
odd = []
index = -1
while command != 'end':
    list_index = []
    command_list = command.split(' ')
    if command_list[0] == 'exchange':
        if 0 <= int(command_list[-1]) < len(nums):
            listA = nums[:int(command_list[-1]) + 1]
            listB = nums[int(command_list[-1]) + 1:]
            nums = listB + listA
            even = []
            odd = []
        else:
            print("Invalid index")
        for i in nums:
            if int(i) % 2 == 0:
                even.append(int(i))
            else:
                odd.append(int(i))

    elif command_list[0] == 'max':
        if command_list[-1] == 'even':
            if len(even) != 0:
                max_v = max(even)
                index = even.index(max_v)
                print(index)
            else:
                print("No matches")
        else:
            if len(odd) != 0:
                max_v = max(odd)
                index = odd.index(max_v)
                print(index)
            else:
                print("No matches")


    elif command_list[0] == 'min':
        if command_list[-1] == 'even':
            if len(even) != 0:
                max_v = max(even)
                index = even.index(max_v)
                print(index)
            else:
                print("No matches")
        else:
            if len(odd) != 0:
                min_v = min(odd)
                index = odd.index(min_v)
                print(index)
            else:
                print("No matches")
    elif command_list[0] == 'first':
        if command_list[-1] == 'even':
            if 0 <= int(command_list[1]) < len(even):
                if len(even) != 0:
                    list_index = even[:int(command_list[1])]
                    print(list_index)
                else:
                    print(list_index)
            else:
                print("Invalid count")

        else:
            if 0 <= int(command_list[1]) < len(odd):
                if len(odd) != 0:
                    list_index = odd[:int(command_list[1])]
                    print(list_index)
                else:
                    print(list_index)
            else:
                print("Invalid count")



    elif command_list[0] == 'last':
        if command_list[-1] == 'even':
            if 0 <= int(command_list[1]) < len(even):
                if len(even) != 0:
                    list_index = even[int(len(even)) - int(command_list[1]):]
                    print(list_index)
                else:
                    print(list_index)
            else:
                print("Invalid count")
        else:
            if 0 <= int(command_list[1]) < len(odd):
                if len(odd) != 0:
                    list_index = odd[int(len(even)) - int(command_list[1]):]
                    print(list_index)
                else:
                    print(list_index)
            else:
                print(list_index)

    command = input()
print(nums)
