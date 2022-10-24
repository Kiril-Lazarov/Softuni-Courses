# text = input()
# new_pass = ''
# while True:
#     command = input()
#     if command == "Done":
#         break
#     command = command.split()
#     if command[0] == "TakeOdd":
#         new_pass = ''
#         for i in range(len(text)):
#             if i %2 != 0:
#                 new_pass += text[i]
#         text = new_pass
#         print(text)
#     elif command[0] == "Cut":
#         index = int(command[1])
#         length = int(command[2])
#         text = text[:index] + text[index +length:]
#         print(text)
#     elif command[0] == "Substitute":
#         substring = command[1]
#         substitute = command[2]
#         if substring in text:
#             text = text.replace(substring, substitute)
#             print(text)
#         else:
#             print("Nothing to replace!")
# print(f"Your password is: {text}")
string = input()
while True:
    data = input()
    if data == "Done":
        break
    commands = data.split(" ")
    if commands[0] == 'TakeOdd':
        string = "".join([string[char] for char in range(len(string)) if char % 2 == 1])
        print(string)
    elif commands[0] == 'Cut':
        string = string.replace("".join(string[int(commands[1]):int(commands[1]) + int(commands[2])]), "", 1)
        print(string)
    elif commands[0] == 'Substitute':
        if commands[1] in string:
            string = string.replace(commands[1], commands[2])
            print(string)
        else:
            print("Nothing to replace!")
print(f"Your password is: {string}")