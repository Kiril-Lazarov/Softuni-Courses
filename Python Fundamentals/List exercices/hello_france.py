items_list = input().split('|')
budget = float(input())
initial_budget = budget
final_list = []
isSmaller = False
price_list = []
new_price_list = []
profit = 0
for i in items_list:
    isSmaller = False
    final_list = i.split('->')
    type = final_list[0]
    price = float(final_list[1])
    if type == 'Clothes':
        if price <= 50.00:
            isSmaller = True
    elif type == 'Shoes':
        if price <= 35.00:
            isSmaller = True
    elif type == 'Accessories':
        if price <= 20.50:
            isSmaller = True
    if isSmaller:
        if budget >= price:
            budget -= price
            price_list.append(f'{float(price)}')
        else:
            break
for j in range(len(price_list)):
    new_price_list.append(f'{float(price_list[j]) * 1.4:.2f}')
    profit += float(price_list[j]) * 1.4
total_profit = profit + budget
print(' '.join(new_price_list))
print(f"Profit: {abs(total_profit-initial_budget):.2f}")
if total_profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")