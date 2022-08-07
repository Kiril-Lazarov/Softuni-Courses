number = int(input())
highest_value = -1
set_weight = 0
set_time = 0
set_quality = 0
for i in range(number):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > highest_value:
        highest_value = value
        set_weight = weight
        set_time = time
        set_quality = quality
print(f"{set_weight} : {set_time} = {highest_value:.0f} ({set_quality})")