month = input()
nights_quantity = int(input())

price_studio = 1
price_apartment = 1
studio_discount = 1
apartment_discount = 1

if nights_quantity > 14:
    apartment_discount = 0.9
else:
    apartment_discount = apartment_discount
if month == 'May' or month == 'October':
    price_studio = 50
    price_apartment = 65
    if 7 < nights_quantity < 14:
        studio_discount = 0.95
    elif nights_quantity > 14:
        studio_discount = 0.7
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartment = 68.70
    if nights_quantity > 14:
        studio_discount = 0.8
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartment = 77

total_price_studio = nights_quantity * price_studio * studio_discount
total_price_apartment =  nights_quantity * price_apartment * apartment_discount

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
