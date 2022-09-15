text = input()
text_dict = {}

for letter in text:
    if letter != ' ':
        if letter not in text_dict:
            text_dict[letter] = 1
        else:
            text_dict[letter] += 1

for key, value in text_dict.items():
    print(f'{key} -> {value}')