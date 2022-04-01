# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
from math import floor, ceil

bloodline_area = int(input())
quantity_grape_per_square_m = float(input())
needed_liters_wine = int(input())
workers_count = int(input())

quantity_area_for_wine_production = bloodline_area * 0.4
total_quantity_grape_for_wine_production = quantity_area_for_wine_production * quantity_grape_per_square_m
wine_production = total_quantity_grape_for_wine_production / 2.5

if wine_production < needed_liters_wine:
    print(f'It will be a tough winter! More {floor(abs(wine_production - needed_liters_wine))} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(wine_production)} liters.')
    print(f'{ceil(wine_production - needed_liters_wine)} liters left -> '
          f'{ceil(ceil(wine_production - needed_liters_wine)/ workers_count)} liters per person.')
# print(quantity_area_for_wine_production, total_quantity_grape_for_wine_production, wine_production)