from collections import deque

ramen = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while True:
    curr_bowl = ramen[-1]
    curr_customer = customers[0]
    if curr_bowl ==  curr_customer:
        ramen.pop()
        customers.popleft()
        if not ramen or not customers:
            break

    elif curr_bowl > curr_customer:
        ramen[-1] -= curr_customer
        customers.popleft()
        if not customers:
            break

    elif curr_bowl < curr_customer:
        customers[0] -= curr_bowl
        ramen.pop()
        if not ramen:
            break
if not customers:
    print(f"Great job! You served all the customers.")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
if ramen:
    print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen])}")
if customers:
    print(f"Customers left: {', '.join([str(x) for x in customers])}")