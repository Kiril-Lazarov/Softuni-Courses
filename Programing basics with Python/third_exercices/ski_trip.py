# •	Първи ред - дни за престой - цяло число в интервала [0...365]
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
# •	Трети ред - оценка - "positive"  или "negative"

days = int(input())
room_type = input()
assessment = input()
price = 0
discount = 0
tip = 0

if room_type == "apartment":
    price = 25
    if days < 10:
        discount = 0.7
    elif 10 <= days <= 15:
        discount = 0.65
    else:
        discount = 0.5
elif room_type == "room for one person":
    price = 18
    discount = 1

elif room_type == "president apartment":
    price = 35
    if days < 10:
        discount = 0.9
    elif 10 <= days <= 15:
        discount = 0.85
    else:
        discount = 0.8
if assessment == "positive":
    tip = 1.25
else:
    tip = 0.9
total_price = (days - 1) * price * discount * tip
print(f'{total_price:.2f}')
# print(days - 1, discount, tip)
