string = input()
string = list(string)

while string:
    letter = string.pop()
    print(letter, end= "")