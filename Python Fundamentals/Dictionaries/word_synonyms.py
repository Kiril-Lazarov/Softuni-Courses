number = int(input())
synonyms = {}

for i in range(number):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key in synonyms.keys():
    list = ", ".join(synonyms[key])
    print(f'{key} - {list}')
