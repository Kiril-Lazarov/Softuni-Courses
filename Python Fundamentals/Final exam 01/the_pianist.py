# n = int(input())
# pieces = {}
# for i in range(n):
#     data = input().split('|')
#     pieces[data[0]] = [data[1], data[2]]
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#     command = command.split('|')
#     if command[0] == 'Add':
#         if command[1] in pieces:
#             print(f"{command[1]} is already in the collection!")
#         else:
#             pieces[command[1]] = [command[2], command[3]]
#             print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
#     elif command[0] == 'Remove':
#         if command[1] in pieces:
#             del pieces[command[1]]
#             print(f"Successfully removed {command[1]}!")
#         else:
#             print(f"Invalid operation! {command[1]} does not exist in the collection.")
#     elif command[0] == 'ChangeKey':
#         if command[1] in pieces:
#             pieces[command[1]][1] = command[2]
#             print(f"Changed the key of {command[1]} to {command[2]}!")
#         else:
#             print(f"Invalid operation! {command[1]} does not exist in the collection.")
# for key, value in pieces.items():
#     print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
#
n = int(input())
composers = {}
for i in range(n):
    data = input().split("|")
    if data[0] not in composers:
        composers[data[0]] = {data[1]: data[2]}
while True:
    info = input()
    if info == "Stop":
        break
    actions = info.split("|")
    piece = actions[1]
    if actions[0] == 'Add':
        key = actions[3]
        composer = actions[2]
        if piece not in composers:
            print(f"{piece} by {composer} in {key} added to the collection!")
            composers[piece] = {composer: key}
        else:
            print(f"{piece} is already in the collection!")
    elif actions[0] == 'Remove':
        if piece in composers:
            del composers[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif actions[0] == 'ChangeKey':
        key = actions[2]
        if piece in composers:
            for composer, value in composers[piece].items():
                composers[piece][composer] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
for piece in composers:
    for composer, key in composers[piece].items():
        print(f"{piece} -> Composer: {composer}, Key: {key}")
