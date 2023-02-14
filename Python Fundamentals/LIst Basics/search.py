n = int(input())
word = input()
full_list = []
word_list = []
for i in range(n):
    string = input()
    full_list.append(string)
    if word in string:
        word_list.append(string)
print(full_list)
print(word_list)