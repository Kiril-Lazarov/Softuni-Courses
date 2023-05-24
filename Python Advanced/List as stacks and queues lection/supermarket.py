from collections import deque

clients = deque()
while True:
    customers = input()
    if customers == "End":
        print(f'{len(clients)} people remaining.')
        break

    elif customers == "Paid":
        while clients:
            client = clients.popleft()
            print(client)
    else:
        clients.append(customers)