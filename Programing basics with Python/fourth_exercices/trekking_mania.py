# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест

# groups_count = int(input())
# total_people = 0
#
# group1 = 0
# group2 = 0
# group3 = 0
# group4 = 0
# group5 = 0
#
# for groups in range(groups_count):
#     people_count = int(input())
#     total_people += people_count
#     if people_count < 6:
#         group1 += people_count
#     elif people_count < 13:
#         group2 += people_count
#     elif people_count < 26:
#         group3 += people_count
#     elif people_count < 41:
#         group4 += people_count
#     else:
#         group5 += people_count
#     percent1 = group1 / total_people * 100
#     percent2 = group2 / total_people * 100
#     percent3 = group3 / total_people * 100
#     percent4 = group4 / total_people * 100
#     percent5 = group5 / total_people * 100
# print(f'{percent1:.2f}%')
# print(f'{percent2:.2f}%')
# print(f'{percent3:.2f}%')
# print(f'{percent4:.2f}%')
# print(f'{percent5:.2f}%')

# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест

count_group = int(input())
Mussala = 0
Monblan = 0
Kilimanjaro = 0
K2 = 0
Everest = 0
all_people = 0
for i in range(count_group):
    count_people = int(input())
    if 1 <= count_people <= 5:
        Mussala += count_people
    elif count_people <= 12:
        Monblan += count_people
    elif count_people <= 25:
        Kilimanjaro += count_people
    elif count_people <= 40:
        K2 += count_people
    elif count_people > 40:
        Everest += count_people
    all_people += count_people
Mussala_percent = Mussala / all_people * 100
Monblan_percent = Monblan / all_people * 100
Kilimanjaro_percent = Kilimanjaro/ all_people * 100
K2_percent = K2 / all_people * 100
Everest_percent = Everest / all_people * 100


print(f'{Mussala_percent:.2f}%')
print(f'{Monblan_percent:.2f}%')
print(f'{Kilimanjaro_percent:.2f}%')
print(f'{K2_percent:.2f}%')
print(f'{Everest_percent:.2f}%')


