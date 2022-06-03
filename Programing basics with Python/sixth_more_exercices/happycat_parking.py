# •	Брой дни – цяло число в интервала [1 … 5]
# •	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]

days_count = int(input())
hours_count = int(input())

regular_price = 0
final_sum = 0
for days in range(1, days_count + 1):
    days_sum = 0
    for hours in range(1, hours_count + 1):
        if days % 2 == 0 and hours % 2 == 1:
            regular_price = 2.5
        elif days % 2 == 1 and hours % 2 == 0:
            regular_price = 1.25
        else:
            regular_price = 1
        days_sum += regular_price
    print(f"Day: {days} - {days_sum:.2f} leva")
    final_sum += days_sum
print(f"Total: {final_sum:.2f} leva")