from collections import deque

cups = deque([int(x) for x in input().split(' ')])
bottles = [int(x) for x in input().split(' ')]
wasted_water = 0
while True:
    curr_bottle = bottles.pop()
    curr_cupp = cups.popleft()
    if curr_bottle > curr_cupp:
        wasted_water += curr_bottle - curr_cupp
    elif curr_bottle < curr_cupp:
        curr_cupp -= curr_bottle
        cups.appendleft(curr_cupp)
    if not cups or not bottles:
        break
if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}" )
if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")
