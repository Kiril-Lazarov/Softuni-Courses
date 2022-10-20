# import  re
# n = int(input())
# plants = {}
# for i in range(n):
#     data = input().split("<->")
#     plants[data[0]]= [int(data[1])]
#
#
# while True:
#     command = input()
#     if command == "Exhibition":
#         break
#     command = re.findall(r"[A-Za-z0-9]+", command)
#     name = command[1]
#     if name in plants:
#         if command[0] == 'Rate':
#             rate = int(command[2])
#             plants[name].append(rate)
#         elif command[0] == 'Update':
#             plants[name][0] = int(command[2])
#         elif command[0] == 'Reset':
#             plants[name] = plants[name][:1]
#     else:
#         print('error')
# print("Plants for the exhibition:")
# for key, value in plants.items():
#     if len(value[1:]) == 0:
#         average = 0
#     else:
#         average = sum(value[1:])/(len(value[1:]))
#     print(f'- {key}; Rarity: {value[0]}; Rating: {average:.2f}')
n = int(input())
plants = {}
for i in range(n):
    data = input().split("<->")
    plants[data[0]] = [int(data[1])]

while True:
    info = input()
    if info == "Exhibition":
        break
    actions = info.split(": ")
    actions[1] = actions[1].split(" - ")
    if actions[1][0] not in plants:
        print("error")
    else:
        if actions[0] == 'Rate':
            plants[actions[1][0]].append(int(actions[1][1]))
        elif actions[0] == 'Update':
            plants[actions[1][0]][0]= int(actions[1][1])
        elif actions[0] == 'Reset':
            plants[actions[1][0]] = plants[actions[1][0]][:1]
print("Plants for the exhibition:")
for keys, values in plants.items():
    if len(values[1:]) != 0:
        average = sum(values[1:]) / len(values[1:])
    else:
        average = 0
    print(f"- {keys}; Rarity: {values[0]}; Rating: {average:.2f}")