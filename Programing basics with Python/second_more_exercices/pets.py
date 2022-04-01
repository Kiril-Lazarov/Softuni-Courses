# •	Първи ред – брой дни – цяло число в интервал [1…5000]
# •	Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# •	Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# •	Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# •	Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
from math import floor, ceil
days_count = int(input())
leaved_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day_grams = float(input())

total_food_for_all = (dog_food_per_day + cat_food_per_day + turtle_food_per_day_grams / 1000) * days_count
if total_food_for_all - leaved_food <= 0:
    print(f'{floor(leaved_food - total_food_for_all)} kilos of food left.')
else:
    print(f'{ceil(total_food_for_all - leaved_food)} more kilos of food are needed.')
