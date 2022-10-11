#
#
# final_string = input()
# message = list(final_string)
#
#
# while True:
#     command = input()
#     if command == 'Reveal':
#         break
#     command = command.split(":|:")
#     if command[0] == 'InsertSpace':
#         message.insert(int(command[1]), ' ')
#         final_string = ''.join(message)
#         print(final_string)
#     elif command[0] == 'Reverse':
#         if command[1] in final_string:
#             list = list(command[1])
#             start_index = final_string.index(list[0])
#             del message[start_index: start_index + len(list)]
#             message += list[::-1]
#             final_string = ''.join(message)
#             print(final_string)
#         else:
#             print('error')
#     elif command[0] == 'ChangeAll':
#         if command[1] in final_string:
#             final_string = final_string.replace(command[1], command[2])
#             message = list(final_string)
#         print(final_string)
#
# print(f"You have a new text message: {final_string}")
message = input()
while True:
    data = input()
    if data == "Reveal":
        break
    commands = data.split(":|:")
    if commands[0] == 'InsertSpace':
        message = message[:int(commands[1])] + ' ' + message[int(commands[1]):]
        print(message)
    elif commands[0] == 'Reverse':
        substring = commands[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message + substring[::-1]
            print(message)
        else:
            print("error")
    elif commands[0] == 'ChangeAll':
        substring = commands[1]
        replacement = commands[2]
        message = message.replace(substring, replacement)
        print(message)
print(f"You have a new text message: {message}")