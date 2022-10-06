# import re
#
#
# def check_valids(final_dict):
#     count = len(final_dict)
#     final_list = []
#     if count == 0:
#         print("No word pairs found!")
#         print("No mirror words!")
#     else:
#         print(f"{count} word pairs found!")
#         for key, value in final_dict.items():
#             if value[::-1] == key:
#                 final_list.append(f'{key} <=> {value}')
#         for i in range(len(final_list)):
#             if "@" in final_list[i]:
#                 final_list[i] = final_list[i].replace('@', '')
#             if '#' in final_list[i]:
#                 final_list[i] = final_list[i].replace('#', '')
#         if len(final_list) == 0:
#             print("No mirror words!")
#         else:
#             print('The mirror words are:')
#             print(', '.join(final_list))
#
#
# def inputs():
#     final_dict = {}
#     text = input()
#     words = re.finditer(r"@(?P<monkey>[a-zA-Z]{3,}@@[a-zA-Z]{3,}@)|#(?P<square>[a-zA-Z]{3,}##[a-zA-Z]{3,}#)", text)
#     for word in words:
#         pairs = []
#         number = int(len(word.group()) / 2)
#         pairs.append(word.group())
#         final_dict[pairs[0][:number]] = pairs[0][number:]
#
#     check_valids(final_dict)
#
#
# inputs()
import re
text = input()
matched_words = {}
words = re.findall(r"@[A-Za-z]{3,}@@[A-Za-z]{3,}@|#[A-Za-z]{3,}##[A-Za-z]{3,}#", text)
if len(words) == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    for word in words:
        delimiter = int(len(word) / 2)
        current_word = word[delimiter + 1:-1]
        if word[1:delimiter - 1] == current_word[::-1]:
            matched_words[word[1:delimiter - 1]] = current_word
    print(f"{len(words)} word pairs found!")
    if len(matched_words) == 0:
        print("No mirror words!")
    else:
        final_list = []
        print("The mirror words are:")
        for key, value in matched_words.items():
            final_list.append(f'{key} <=> {value}')
        print(", ".join(final_list))
