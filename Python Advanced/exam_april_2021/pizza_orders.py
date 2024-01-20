from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees = deque([int(x) for x in input().split(', ')])
total_pizza = 0

while True:
    if pizza_orders[0]<= 0:
        pizza_orders.popleft()
        if not pizza_orders:
            break
        else:
            continue
    if employees[-1] <=0:
        employees.pop()
        if not employees:
            break
        else:
            continue
    if pizza_orders[0] > 10:
        pizza_orders.popleft()
        if not pizza_orders:
            break
        continue
    if pizza_orders[0]<= employees[-1]:
        employees.pop()
        total_pizza += pizza_orders.popleft()
        if not pizza_orders:
            break
        if not employees:
            break
    else:
        total_pizza += employees[-1]
        pizza_orders[0] -= employees[-1]
        employees.pop()
        if not employees:
            break



if not pizza_orders:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {total_pizza}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')
if not employees:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')
