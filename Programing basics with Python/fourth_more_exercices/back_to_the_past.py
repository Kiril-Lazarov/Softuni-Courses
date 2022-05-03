# •	Наследените пари – реално число в интервала [1.00 ... 1 000 000.00]
# •	Годината, до която трябва да живее (включително) – цяло число в интервала [1801 ... 1900]

legacy_money = float(input())
year = int(input())
cost = 0

for i in range (1800, year+1):
    if i%2 == 1:
        cost += 12000 + 50 * (18 + i-1800)
    else:
        cost += 12000

if legacy_money >= cost:
    print(f"Yes! He will live a carefree life and will have {legacy_money - cost:.2f} dollars left.")
else:
    print(f"He will need {cost-legacy_money:.2f} dollars to survive." )


    # print(i)
