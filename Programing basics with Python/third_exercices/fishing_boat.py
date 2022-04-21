# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.

budget = int(input())
season = input()
number_fishing_men = int(input())

boat_rent = 0
discount = 0
additional_discount = 1
# final_price = boat_rent * discount * additional_discount

if season == 'Spring':
    boat_rent = 3000
    if number_fishing_men <= 6:
        discount = 0.9
    elif 7 <= number_fishing_men <= 11:
        discount = 0.85
    elif number_fishing_men >= 12:
        discount = 0.75
    pass

elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
    if number_fishing_men <= 6:
        discount = 0.9
    elif 7 <= number_fishing_men <= 11:
        discount = 0.85
    elif number_fishing_men >= 12:
        discount = 0.75

elif season == 'Winter':
    boat_rent = 2600
    if number_fishing_men <= 6:
        discount = 0.9
    elif 7 <= number_fishing_men <= 11:
        discount = 0.85
    elif number_fishing_men >= 12:
        discount = 0.75
if number_fishing_men % 2 == 0 and season != 'Autumn':
    additional_discount = 0.95
else:
    additional_discount = additional_discount
if budget >= boat_rent * discount * additional_discount:
    print(f"Yes! You have {budget-boat_rent * discount * additional_discount:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_rent * discount * additional_discount - budget:.2f} leva.")