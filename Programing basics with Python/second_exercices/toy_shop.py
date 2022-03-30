vacation_price = float(input())
puzzle_number = int(input())
talking_dolls_number = int(input())
bear_number = int(input())
minions_number = int(input())
trucks_number = int(input())

sum_numbers_toys = puzzle_number + talking_dolls_number + bear_number + minions_number + trucks_number
profit_from_toys = puzzle_number * 2.60 + talking_dolls_number * 3 + bear_number * 4.10 + minions_number * 8.20 + trucks_number * 2

if sum_numbers_toys >= 50:
    money_left = profit_from_toys * 0.75 * 0.9 - vacation_price
    if money_left >= 0:
         print(f'Yes! {abs(money_left):.2f} lv left.')
    else:
        print(f'Not enough money! {abs(money_left):.2f} lv needed.')
else:
    money_left = profit_from_toys * 0.9 - vacation_price
    if money_left >= 0:
         print(f'Yes! {abs(money_left):.2f} lv left.')
    else:
        print(f'Not enough money! {abs(money_left):.2f} lv needed.')