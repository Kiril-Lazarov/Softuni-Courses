import re

password = input()

while True:
    data = input()
    if data == "Complete":
        break
    commands = data.split(" ")
    if commands[0] == 'Make':
        index = int(commands[2])
        if commands[1] == "Upper":
            new_sym = password[index].upper()

        else:
            new_sym = password[index].lower()
        password = password[:index] + new_sym + password[index+1:]
        print(password)
    elif commands[0] == 'Insert':
        if  0 <=int(commands[1]) <len(password):
            password = password[:int(commands[1])] + commands[2] + password[int(commands[1]):]
            print(password)
    elif commands[0] == 'Replace':
        char = commands[1]
        if char in password:
            value = int(commands[2])
            new_char = ord(char) + value
            password = password.replace(char, chr(new_char))
            print(password)
    elif commands[0] == 'Validation':
        test_password_for_non_word = re.findall(r"[^A-Za-z0-9_]", password)
        test_password_for_upper = re.findall(r"[A-Z]", password)
        test_password_for_lower = re.findall(r"[a-z]", password)
        test_password_for_digits = re.findall(r"[\d]", password)
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if len(test_password_for_non_word) != 0:
            print("Password must consist only of letters, digits and _!")
        if len(test_password_for_upper) == 0:
            print("Password must consist at least one uppercase letter!")
        if len(test_password_for_lower) == 0:
            print("Password must consist at least one lowercase letter!")
        if len(test_password_for_digits) == 0:
            print("Password must consist at least one digit!")

