from collections import deque

children = deque()

info = input().split(' ')

for name in info:
    children.append(name)
number = int(input())
count = 0
while True:
    if len(children) == 1:
        break
    for i in range(number):
        if i != number -1:
            buffer = children.popleft()
            children.append(buffer)
        else:
            looser = children.popleft()
            print(f"Removed {looser}" )

print(f"Last is {children[0]}")


