string = input().split(' ')
for i in range(len(string)):
    word = list(string[i])
    number = ''
    for k in range(len(word)):
        if 48 <= ord(word[k]) <= 57:
            number += word[k]

    letter = chr(int(number))
    for j in range(len(number)):
        word.remove(number[j])
    word.insert(0, letter)
    word[1], word[-1] = word[-1], word[1]
    string[i] = ''.join(word)

print(' '.join(string))
