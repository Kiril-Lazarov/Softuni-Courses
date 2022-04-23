# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.

flower = input()
flower_count = int(input())
budget = int(input())

Rose = 5
Dahlias = 3.80
Tulip = 2.80
Narcissus = 3
Gladiolus = 2.50
discount = 1
final_sum = flower_count * discount

if flower == 'Roses':
    if flower_count > 80:
        discount = 0.9
        final_sum = flower_count * Rose * discount
    else:
        discount = discount
        final_sum = flower_count * Rose * discount
elif flower == 'Dahlias':
    if flower_count > 90:
        discount = 0.85
        final_sum = flower_count * Dahlias * discount
    else:
        discount = discount
        final_sum = flower_count * Dahlias * discount
elif flower == 'Tulips':
    if flower_count > 80:
        discount = 0.85
        final_sum = flower_count * Tulip * discount
    else:
        discount = discount
        final_sum = flower_count * Tulip * discount
elif flower == 'Narcissus':
    if flower_count < 120:
        discount = 1.15
        final_sum = flower_count * Narcissus * discount
    else:
        discount = discount
        final_sum = flower_count * Narcissus * discount
elif flower == 'Gladiolus':
    if flower_count < 80:
        discount = 1.2
        final_sum = flower_count * Gladiolus * discount
    else:
        discount = discount
        final_sum = flower_count * Gladiolus * discount
if budget >= final_sum:
    print(f"Hey, you have a great garden with {flower_count} {flower} and {budget - final_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_sum - budget:.2f} leva more.")