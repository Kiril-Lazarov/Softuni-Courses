# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]

budget = float(input())
category = input()
people_count = int(input())
percent = 1
price_ticket = 1

if 1 <= people_count <= 4:
    percent = 0.25
elif 5 <= people_count <= 9:
    percent = 0.4
elif 9 <= people_count <= 24:
    percent = 0.5
elif 25 <= people_count <= 49:
    percent = 0.6
elif people_count > 49:
    percent = 0.75
if category == "VIP":
    price_ticket = 499.99
else:
    price_ticket = 249.99
total_price = people_count * price_ticket
sum_total = budget * percent - total_price

if sum_total >= 0:
    print(f"Yes! You have {sum_total:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(sum_total):.2f} leva.")

# print(total_price, sum_total)