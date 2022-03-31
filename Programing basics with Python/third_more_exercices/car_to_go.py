# # •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# # •	Втори ред –  Сезон – текст "Summer" или "Winter"
#
# •	При бюджет по-малък или равен от 100лв.:
# o	Класът ще е - "Economy class"
# o	Според сезона колата и цената ще са:
# 	Лято – Кабрио – 35% от бюджета
# 	Зима – Джип – 65% от бюджета
# •	При бюджет по-голям от 100лв. и по-малък или равен от 500лв.:
# o	Класът ще е - "Compact class"
# o	Според сезона колата и цената ще са:
# 	Лято – Кабрио – 45% от бюджета
# 	Зима – Джип – 80% от бюджета
# •	При бюджет по-голям от 500лв.:
# o	Класът ще е – "Luxury class"
# o	За всеки сезон колата ще е джип и цената ще е:
# 	90% от бюджета

budget = float(input())
season = input()

discount = 1
car_class = ""
type_car = ""

if budget <= 100:
    car_class = 'Economy class'
    if season == "Summer" :
        type_car = "Cabrio"
        discount = 0.35
    else:
        type_car = "Jeep"
        discount = 0.65

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        discount = 0.45
    else:
        type_car = "Jeep"
        discount = 0.8
else:
    car_class = "Luxury class"
    discount = 0.9
    type_car = "Jeep"
rent_price = budget * discount
print(f"{car_class}")
print(f'{type_car} - {rent_price:.2f}')
