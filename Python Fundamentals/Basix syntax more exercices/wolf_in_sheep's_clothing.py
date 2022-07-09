# list1 = []
# word = ''
# queue = input()
# for i in range(len(queue)):
#     if ord(queue[i]) != 44:
#         word += queue[i]
#     else:
#         list1.append(word)
#         word = ''
# list1.append(word)
# stored_index = 0
# last_index = len(list1)
# sheep_position_counter = 0
# isWolf = False
# for i in range(len(list1)):
#     if list1[i] == 'wolf' or list1[i] == ' wolf':
#         isWolf = True
#         sheep_position_counter = - 1
#     if isWolf or list[i] == 'sheep':
#         sheep_position_counter +=1
# if sheep_position_counter == 0:
#     print("Please go away and stop eating my sheep")
# else:
#
#     print(f"Oi! Sheep number {sheep_position_counter}! You are about to be eaten by a wolf!" )


string = input()
list1= []
list2 = []
index_wolf_position = 0
for i in range(len(string)):
    if string[i] == 'w' or string[i] == 's':
        if string[i] == 's':
            list1.append('sheep')
        elif string[i] == 'w':
            list1.append('wolf')
index_wolf_position = len(list1)
for j in range(len(list1)):
    if list1[j] == 'sheep':
        list2.append(len(list1) - j)
    elif list1[j] == 'wolf':
        list2.append('wolf')
        index_wolf_position = j

if index_wolf_position == len(list2) -1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {list2[index_wolf_position + 1]}! You are about to be eaten by a wolf!" )
# print(list1)
# print(list2)
