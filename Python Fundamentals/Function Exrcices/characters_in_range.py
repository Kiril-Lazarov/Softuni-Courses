def string_characters(a, b):
    char_string = ''
    for i in range(ord(char1)+1, ord(char2)):
        char_string += chr(i) + ' '
    return char_string



char1, char2 = input(), input()

print(string_characters(char1, char2))