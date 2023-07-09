from collections import deque

n = int(input())
initial_pumps = deque()
for i in range(n):
    info = list(map(int, input().split(' ')))
    initial_pumps.append((info[0], info[1]))
litters = 0
attempts = 0
index = 0
while True:
    attempts += 1
    if litters + initial_pumps[attempts-1][0] - initial_pumps[attempts-1][1] < 0:
        initial_pumps.append(initial_pumps.popleft())
        index += 1
        attempts = 0
        litters = 0
    else:
        litters += initial_pumps[attempts-1][0] - initial_pumps[attempts-1][1]

        if attempts == n:
            if (litters + initial_pumps[attempts-1][0] - initial_pumps[attempts-1][0])>=0:
                print(index)
                break
            else:
                initial_pumps.append(initial_pumps.popleft())
                index += 1
                attempts = 0
                litters = 0

