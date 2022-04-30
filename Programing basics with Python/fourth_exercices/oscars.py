# •	Име на актьора - текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n - цяло число в интервала[1… 20]

actor_name = input()
initial_points = float(input())
count_jury = int(input())
name_lenght = 0
result = 0
for count_jury in range(count_jury):
    jury_name = input()
    points_given_by_jury_name = float(input())
    name_lenght = len(jury_name)
    initial_points += name_lenght * points_given_by_jury_name / 2
    if initial_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {initial_points:.1f}!")
        break
if initial_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5-initial_points:.1f} more!")