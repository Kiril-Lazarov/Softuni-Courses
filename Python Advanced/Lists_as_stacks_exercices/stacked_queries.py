n = int(input())
stack = []
for i in range(n):
    command = input()
    if command.startswith("1 "):
        stack.append(int(command.split(' ')[1]))
    if stack:
        if command == '2':

                stack.pop()
        elif command == '3':
            print(max(stack))
        elif command == '4':
            print(min(stack))
new_stack = []
if stack:
    while stack:
        new_stack.append(stack.pop())
    print(', '.join(map(str, new_stack)))
