# import re
#
# text = input()
#
# valid_words = re.findall(r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*", text)
# number_valid_words = len(valid_words)
# numbers = re.findall(r"[\d]", text)
# coolness_dict = {}
# cool_num = 1
# for i in numbers:
#     cool_num *= int(i)
# for words in valid_words:
#     new_words = re.findall(r'[A-Za-z]+', words)
#     sum_ascii = 0
#     for i in ''.join(new_words):
#         sum_ascii += ord(i)
#     if sum_ascii > cool_num:
#         coolness_dict[''.join(words)] = sum_ascii
# print(f"Cool threshold: {cool_num}")
# print(f"{number_valid_words} emojis found in the text. The cool ones are:")
# for key in coolness_dict:
#     print(key)

import re
from functions  import  product_nums, ascii_sum

text = input()

words = re.findall(r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*", text)
numbers = product_nums(" ".join(re.findall(r"[\d]", text)))
print(f"Cool threshold: {numbers}")
print(f"{len(words)} emojis found in the text.")
print("The cool ones are:")
for i in words:
    if ascii_sum(i[2:-2])>numbers:
        print(i)





