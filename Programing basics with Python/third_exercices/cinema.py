# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.


type_projection = input()
rows = int(input())
columns = int(input())

Premiere = 12.00
Normal = 7.50
Discount = 5.00

if type_projection == "Premiere":
    total_income = rows * columns * Premiere
elif type_projection == 'Normal':
    total_income = rows * columns * Normal
elif type_projection == 'Discount':
    total_income = rows * columns * Discount
print(f'{total_income:.2f} leva')


