from collections import deque

bullet_price = int(input())
size_barrel = int(input())
total_bulets_cost = 0
bullets = [int(x) for x in input().split(' ')]
locks = deque([int(x) for x in input().split(' ')])
intelligence = int(input())
fired_bullets = 0
success = False
while True:
    curr_bullet = bullets.pop()
    curr_lock = locks.popleft()
    fired_bullets += 1
    total_bulets_cost += bullet_price
    if curr_lock < curr_bullet:
        print('Ping!')
        locks.appendleft(curr_lock)
    else:
        print('Bang!')
    if not locks and not bullets:
        success = True
        break


    if not bullets:
        break
    if size_barrel == fired_bullets:
        print('Reloading!')
        fired_bullets = 0
    if not locks:
        success = True
        break

if success:
    print(f'{len(bullets)} bullets left. Earned ${intelligence - total_bulets_cost}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

