# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].

season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

price = 1
sport = ''
discount = 1
if season == 'Winter':
    if type_of_group == 'girls':
        price = 9.6
        sport = 'Gymnastics'
    elif type_of_group == 'boys':
        price = 9.6
        sport = 'Judo'
    else:
        price = 10
        sport = 'Ski'
elif season == 'Spring':
    if type_of_group == 'girls':
        price = 7.2
        sport = 'Athletics'
    elif type_of_group == 'boys':
        price = 7.2
        sport = 'Tennis'
    else:
        price = 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if type_of_group == 'girls':
        price = 15
        sport = 'Volleyball'
    elif type_of_group == 'boys':
        price = 15
        sport = 'Football'
    else:
        price = 20
        sport = 'Swimming'
if students_count >= 50:
    discount = 0.5
elif 20 <= students_count < 50:
    discount = 0.85
elif 10 <= students_count < 20:
    discount = 0.95

total_price = students_count * nights_count * price * discount
print(f"{sport} {total_price:.2f} lv.")

