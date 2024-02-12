from collections import deque

vowels = deque(input().split(' '))
consonants = deque(input().split(' '))

words = {
    "rose": [],
    "tulip": [],
    "lotus": [],
    "daffodil": []
}
word_found = False
word = ''
while True:
    if not vowels or not consonants:
        break
    vowel = vowels.popleft()
    cons = consonants.pop()

    for flower, lists in words.items():
        if vowel in flower and vowel not in lists:
            words[flower].append(vowel)
            if len(flower) == len(words[flower]):
                word_found = True
                word = flower
                break
        if cons in flower and cons not in lists:
            if cons == 'f' or cons == 'd':
                words[flower].append(cons)
                words[flower].append(cons)
            else:
                words[flower].append(cons)
            if len(flower) == len(words[flower]):
                word_found = True
                word = flower
                break
    if word_found:
        break

if word_found:
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
