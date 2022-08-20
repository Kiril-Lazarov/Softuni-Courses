stocks = input().split(': ')
inventory = {}
while stocks[0] != 'statistics':
    if stocks[0] not in inventory:
        inventory[stocks[0]] = int(stocks[1])
    else:
        inventory[stocks[0]] += int(stocks[1])

    stocks = input().split(': ')
print('Products in stock:')
sum_quantity = 0
for key in inventory.keys():
    food = key
    quantity = int(inventory[key])
    print(f'- {food}: {quantity}')
    sum_quantity += quantity
print(f'Total Products: {len(inventory)}')
print(f"Total Quantity: {sum(inventory.values())}")