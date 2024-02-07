from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0
while males and females:
    # if males[-1] <= 0 and females[0] <=0:
    #     males.pop()
    #     females.popleft()
    #     continue
    if females[0]<=0 and males[-1]<=0:
        females.popleft()
        males.pop()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] % 25 == 0 and females[0] % 25== 0:
        males.pop()
        males.pop()
        females.popleft()
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] == females[0]:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -=2
males = list(males)
females = list(females)

print(f'Matches: {matches}')
if not males:
    word = 'none'
else:
    word = f'{", ".join([str(x) for x in males[::-1]])}'
print(f'Males left: {word}')

if not females:
    word = 'none'
else:
    word = f'{", ".join([str(x) for x in females])}'
print(f'Females left: {word}')
