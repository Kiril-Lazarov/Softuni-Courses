# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]

month_count =int(input())
electricity = 0
water = 0
internet = 0
others = 0
for i in range(month_count):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15
    others = (electricity + water + internet) * 1.2
average = (electricity + water + internet + others) / month_count
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")


