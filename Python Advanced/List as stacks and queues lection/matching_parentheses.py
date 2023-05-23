expression = list(input())
list_open_indexes = []
for i in range(len(expression)):
    if expression[i] == "(":
       list_open_indexes.append(i)
    elif expression[i] == ")":
        index = list_open_indexes.pop()
        print(f'{"".join(expression[index:i+1])}')
