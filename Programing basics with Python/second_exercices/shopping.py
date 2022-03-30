# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [1…100]
# 3.	Броят процесори - цяло число в интервала [1…100]
# 4.	Броят рам памет - цяло число в интервала [1…100]

budget = float(input())
videocards_count = int(input())
processors_count = int(input())
ram_count = int(input())
total_sum = videocards_count * 250 + processors_count * 0.35 * videocards_count * 250 + ram_count * 0.1 \
            * videocards_count * 250
if videocards_count > processors_count:
    total_sum = total_sum * 0.85
    result = budget - total_sum
    if result >= 0:
        print(f"You have {abs(result):.2f} leva left!")
    else:
        print(f"Not enough money! You need {abs(result):.2f} leva more!")
else:
    result = budget - total_sum
    if result >= 0:
        print(f"You have {abs(result):.2f} leva left!")
    else:
        print(f"Not enough money! You need {abs(result):.2f} leva more!")
