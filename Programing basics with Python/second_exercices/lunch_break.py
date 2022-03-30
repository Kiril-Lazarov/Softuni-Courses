from math import ceil, floor

film_name = input()
ep_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4
total_time = break_duration - (ep_duration + lunch_time + rest_time)

if total_time >= 0:
    print(f"You have enough time to watch {film_name} and left with {abs(ceil(total_time))} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you need {abs(floor(total_time))} more minutes.")

