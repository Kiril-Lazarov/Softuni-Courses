text = input()

a = '1'
e = '2'
i = '3'
o = '4'
u = '5'
sum_characters = 0

for character in text:
    if character == 'a':
        sum_characters +=1
    elif character == 'e':
        sum_characters += 2
    elif character == 'i':
        sum_characters += 3
    elif character == 'o':
        sum_characters += 4
    elif character == 'u':
        sum_characters += 5
print(sum_characters)