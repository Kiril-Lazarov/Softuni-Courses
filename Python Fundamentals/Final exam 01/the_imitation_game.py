# message = input()
#
# while True:
#     command = input()
#     if command == "Decode":
#         break
#     shiffer = command.split('|')
#     if shiffer[0] == 'Move':
#         number = int(shiffer[1])
#         seq = message[:number]
#         message = message[number:] + seq
#     elif shiffer[0] == 'Insert':
#         index = int(shiffer[1])
#         value = shiffer[2]
#         message = message[:index] + value + message[index:]
#     elif shiffer[0] == 'ChangeAll':
#         substring = shiffer[1]
#         replacement = shiffer[2]
#         message =message.replace(substring, replacement)
# print(f"The decrypted message is: {message}")
message = input()
while True:
    data = input()
    if data == "Decode":
        break
    actions = data.split("|")
    if actions[0] == 'Move':
        number = int(actions[1])
        piece = message[:number]
        message = message[number:] + piece
    elif actions[0] == 'Insert':
        index = int(actions[1])
        value = actions[2]
        message = message[:index] + value + message[index:]
    elif actions[0] == 'ChangeAll':
        substring = actions[1]
        replacement = actions[2]
        message = message.replace(substring, replacement)
print(f"The decrypted message is: {message}")