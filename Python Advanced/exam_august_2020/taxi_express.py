from collections import deque

customers = deque(int(x)   for x in input().split(', '))
taxis = deque(int(x)   for x in input().split(', '))
total_time = 0
while customers and taxis:
    curr_customer = customers[0]
    curr_taxi = taxis[-1]
    if curr_taxi >= curr_customer:
        total_time += curr_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if not taxis and customers:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(x) for x in customers)}')
elif not customers:
   print('All customers were driven to their destinations')
   print(f'Total time: {total_time} minutes')




