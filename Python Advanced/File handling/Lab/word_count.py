import re

count_words = {}
with open("./words.txt", "w") as file:
    file.write("quick is fault")

with open("./words.txt", 'r') as file:
    for word in file:
        exp = word.split(' ')


with open('./input.txt', 'r') as sentence:
    for s in sentence:

        words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', s)]

        with open("./words.txt", 'r') as main_file:
                for sentence in words_in_line:


                    for word in exp:
                        if word == sentence:
                            if word not in count_words:
                                count_words[word] = 0
                            count_words[word] += 1
sort_list = sorted(count_words.items(), key=lambda x: x[1], reverse= True)
print('\n'.join(f'{key} - {value}' for key, value in sort_list))