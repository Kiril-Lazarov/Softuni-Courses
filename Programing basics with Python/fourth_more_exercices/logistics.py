#
# •	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# •	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)

product_count = int(input())

total_weight = 0
microbus_price = 200
truck_price = 175
train_price = 120
cost = 0
total_weight_microbus = 0
total_weight_truck = 0
total_weight_train = 0

for i in range(product_count):
    weight = int(input())
    total_weight += weight
    if weight < 4:
        cost += weight * microbus_price
        total_weight_microbus += weight
    elif weight < 12:
        cost += weight * truck_price
        total_weight_truck += weight
    else:
        cost += weight * train_price
        total_weight_train += weight
average_cost = cost / total_weight
print(f'{average_cost:.2f}')
print(f'{total_weight_microbus / total_weight * 100:.2f}%')
print(f'{total_weight_truck / total_weight * 100:.2f}%')
print(f'{total_weight_train / total_weight * 100:.2f}%')