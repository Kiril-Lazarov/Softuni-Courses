# •	Първи ред - колко хода ще има по време на играта – цяло число в интервала [1...100]
# •	За всеки ход – числата, които се проверяват в кой интервал са – цели числа в интервала [-100...100]
# •	От 0 до 9  20 % от числото
# •	От 10 до 19  30 % от числото
# •	От 20 до 29  40 % от числото
# •	От 30 до 39  50 точки
# •	От 40 до 50  100 точки
# •	Невалидно число  резултата се дели на 2

stages_game = int(input())
result = 0
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
group6 = 0
for i in range(stages_game):
    num = int(input())
    if 0 <= num < 10:
        result += num * 0.2
        group1 += 1
    elif 10 <= num < 20:
        result += num * 0.3
        group2 += 1
    elif 20 <= num < 30:
        result += num * 0.4
        group3 += 1
    elif 30 <= num < 40:
        group4 += 1
        result += 50
    elif 40 <= num <= 50:
        result += 100
        group5 += 1
    else:
        result /= 2
        group6 += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {group1 / stages_game * 100:.2f}%")
print(f"From 10 to 19: {group2 / stages_game * 100:.2f}%")
print(f"From 20 to 29: {group3 / stages_game * 100:.2f}%")
print(f"From 30 to 39: {group4 / stages_game * 100:.2f}%")
print(f"From 40 to 50: {group5 / stages_game * 100:.2f}%")
print(f"Invalid numbers: {group6 / stages_game * 100:.2f}%")
