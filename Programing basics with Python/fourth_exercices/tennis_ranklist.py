# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
from math import floor

championships_count = int(input())
start_points = int(input())
win_championship_count = 0
gain_points = 0

for champ in range(championships_count):
    reached_stage = input()
    if reached_stage == 'W':
        gain_points += 2000
        win_championship_count += 1
    elif reached_stage == 'F':
        gain_points += 1200
    else:
        gain_points += 720
average_points = gain_points / championships_count
percent_win_championships = win_championship_count / championships_count * 100
print(f"Final points: {gain_points + start_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_win_championships:.2f}%")
