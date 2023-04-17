symbols = {"-", ",", ".", "!", "?"}

with open('./text.txt', 'r') as text:
    lines = text.readlines()
    for i in range(len(lines)):
        if i % 2 == 0:
            for letter in lines[i]:
                if letter in symbols:
                    lines[i] = lines[i].replace(letter, '@')
                if letter == '\n':
                    lines[i] = lines[i].replace(letter, '')
            inverse_sentence = lines[i].split(' ')[::-1]
            print(' '.join(inverse_sentence))


