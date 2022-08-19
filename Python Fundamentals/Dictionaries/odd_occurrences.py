# sequence = input().lower().split(' ')
# sequence_dict = {}
# for word in sequence:
#     count = sequence.count(word)
#     sequence_dict[word] = count
# for i in sequence_dict.items():
#     if i[1] % 2 == 1:
#         print(i[0], end=' ')

words = input().split(' ')
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] +=1

for (x, y) in dictionary.items():
    if y % 2 != 0:
        print(x, end=' ')

