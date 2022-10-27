# activation_keys = input()
#
# while True:
#     command = input()
#     if command == 'Generate':
#         break
#     command = command.split(">>>")
#     if command[0] == "Contains":
#         substring = command[1]
#         if substring in activation_keys:
#             print(f"{activation_keys} contains {substring}")
#         else:
#             print("Substring not found!")
#
#     elif command[0] == "Flip":
#         instruction = command[1]
#         start = int(command[2])
#         end = int(command[3])
#         new_strings = ''
#         for i in range(start, end):
#             if instruction == 'Upper':
#                 new_strings += activation_keys[i].upper()
#             elif instruction == 'Lower':
#                 new_strings += activation_keys[i].lower()
#         activation_keys = activation_keys[:start] + new_strings + activation_keys[end:]
#         print(activation_keys)
#     elif command[0] == "Slice":
#         start = int(command[1])
#         end = int(command[2])
#         activation_keys = activation_keys[:start] + activation_keys[end:]
#         print(activation_keys)
# print(f"Your activation key is: {activation_keys}")
key = input()
while True:
    data = input()
    if data == 'Generate':
        break
    commands = data.split(">>>")
    if commands[0] == 'Contains':
        if commands[1] in key:
            print(f"{key} contains {commands[1]}")
        else:
            print("Substring not found!")
    elif commands[0] == 'Flip':
        start = int(commands[2])
        end = int(commands[3])
        if commands[1] == "Upper":
            key = key[:start] + key[start:end].upper() + key[end:]
        elif commands[1] == "Lower":
            key = key[:start] + key[start:end].lower() + key[end:]
        print(key)

    elif commands[0] == 'Slice':
        start = int(commands[1])
        end = int(commands[2])
        key = key[:start] + key[end:]
        print(key)
print(f"Your activation key is: {key}")
