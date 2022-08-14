key = int(input())
new_letter = 0
word = ''
number_lines = int(input())
for i in range(number_lines):
    letter = input()
    new_letter = ord(letter) + key
    string_letter = chr(new_letter)
    word += string_letter
print(word)