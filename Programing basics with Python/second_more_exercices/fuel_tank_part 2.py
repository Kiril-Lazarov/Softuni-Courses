# •	Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# •	Количество гориво – реално число в интервала [1.00 … 50.00]
# •	Притежание на клубна карта – текст с възможности: "Yes" или "No"

fuel_type = input()
quantity_fuel = float(input())
card_discount_possesion = input()

fuel_price = 1
liters_discount = 1
discount = 0


if 20 <= quantity_fuel <= 25:
    liters_discount = 0.92
    if fuel_type == "Gasoline":
        fuel_price = 2.22
        if card_discount_possesion == "Yes":
            discount = 0.18
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount  * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
    elif fuel_type == "Diesel":
        fuel_price = 2.33
        if card_discount_possesion == "Yes":
            discount = 0.12
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount  * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
    elif fuel_type == "Gas":
        fuel_price = 0.93
        if card_discount_possesion == "Yes":
            discount = 0.08
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
elif quantity_fuel > 25:
    liters_discount = 0.90
    if fuel_type == "Gasoline":
        fuel_price = 2.22
        if card_discount_possesion == "Yes":
            discount = 0.18
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
    elif fuel_type == "Diesel":
        fuel_price = 2.33
        if card_discount_possesion == "Yes":
            discount = 0.12
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
    elif fuel_type == "Gas":
        fuel_price = 0.93
        if card_discount_possesion == "Yes":
            discount = 0.08
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
else:
    liters_discount = 1
    if fuel_type == "Gasoline":
        fuel_price = 2.22
        if card_discount_possesion == "Yes":
            discount = 0.18
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
    elif fuel_type == "Diesel":
        fuel_price = 2.33
        if card_discount_possesion == "Yes":
            discount = 0.12
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')
    elif fuel_type == "Gas":
        fuel_price = 0.93
        if card_discount_possesion == "Yes":
            discount = 0.08
            total_price = quantity_fuel * fuel_price
            print(f'{((total_price - discount * quantity_fuel) * liters_discount):.2f} lv.')
        else:
            total_price = quantity_fuel * fuel_price
            print(f'{(total_price * liters_discount):.2f} lv.')






# print(discount * quantity_fuel,quantity_fuel * fuel_price, total_price )

