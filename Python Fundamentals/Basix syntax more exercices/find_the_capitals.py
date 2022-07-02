string = input()
indeces_list = []
for i in range(len(string)):
    character = string[i]
    if 65<=ord(character)<= 90:
        indeces_list.append(i)
print(indeces_list)