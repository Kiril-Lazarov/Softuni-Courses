from collections import deque
food = int(input())
orders = input()

orders = deque(list(map(int, orders.split())))
print(max(orders))

while orders:
    curr_order = orders[0]
    if curr_order >food:
        break
    food -= curr_order
    orders.popleft()
if orders:
    print(f'Orders left: {" ".join(map(str, orders))}')
else:
    print("Orders complete")
