text = input()
vowels = ['a', 'e', 'i', 'o', 'u']
new_text = [i for i in text if i not in vowels]

print(''.join(new_text))
