season = input()
km_per_month = float(input())
price = 1

if season == 'Spring' or season == 'Autumn':
    if km_per_month <= 5000:
        price = 0.75
    elif 5000 < km_per_month <= 10000:
        price = 0.95
    elif 10000 < km_per_month <= 20000:
        price = 1.45
elif season == 'Summer':
    if km_per_month <= 5000:
        price = 0.9
    elif 5000 < km_per_month <= 10000:
        price = 1.1
    elif 10000 < km_per_month <= 20000:
        price = 1.45
elif season == 'Winter':
    if km_per_month <= 5000:
        price = 1.05
    elif 5000 < km_per_month <= 10000:
        price = 1.25
    elif 10000 < km_per_month <= 20000:
        price = 1.45
profit = km_per_month * 4 * price * 0.9
print(f'{profit:.2f}')