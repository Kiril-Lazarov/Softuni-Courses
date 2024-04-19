
from collections import deque

eggs = deque(int(x) for x in input().split(', '))
paper = [int(x) for x in input().split(', ')]
filled_boxes = 0
first_time_remove_thirteen = False
while True:
    if not eggs and not paper:
        break
    if not eggs:
        break
    if not paper:
        break
    first_egg = eggs.popleft()
    last_paper = paper.pop()
    if first_egg <= 0:
        paper.append(last_paper)
        continue
    if first_egg == 13:
        paper.append(last_paper)
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    if first_egg + last_paper <= 50:
        filled_boxes += 1

if filled_boxes >0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(str(x)for x in eggs)}')
if paper:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper)}')

