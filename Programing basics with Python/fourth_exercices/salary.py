# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [500...1500]

opened_tabs_count = int(input())
salary = float(input())

facebook_count = 0
instagram_count = 0
reddit_count = 0

for i in range(opened_tabs_count):
    site = input()
    if site == "Facebook":
        facebook_count += 1
    elif site == "Instagram":
        instagram_count += 1
    elif site == "Reddit":
        reddit_count += 1
    total_fines = facebook_count * 150 + instagram_count * 100 + reddit_count * 50
if salary - total_fines <= 0:
    print("You have lost your salary.")

else:
    print(f'{salary - total_fines:.0f}')
