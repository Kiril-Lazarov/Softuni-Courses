# •	Възрастта на Лили - цяло число в интервала [1...77]
# •	Цената на пералнята - число в интервала [1.00...10 000.00]
# •	Единична цена на играчка - цяло число в интервала [0...40]

lilli_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
money_count = 0

for birthday in range(1, lilli_age + 1):
    if birthday % 2 == 1:
        toy_count += 1
    else:
        money_count += birthday/2  * 10 -1

total_money = money_count + toy_count * toy_price
if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")

