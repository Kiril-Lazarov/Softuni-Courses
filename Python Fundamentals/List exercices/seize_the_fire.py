info = input().split('#')
water = int(input())
is_in_range = False
effort = 0
total_fire = 0
print("Cells:")
for data in info:
    is_in_range = False
    current_cell = data.split(' = ')
    type_of_fire = current_cell[0]
    level_of_the_fire = int(current_cell[1])
    if type_of_fire == 'High':
        if 81 <= level_of_the_fire <= 125:
            is_in_range = True
    elif type_of_fire == 'Medium':
        if 51 <= level_of_the_fire <= 80:
            is_in_range = True
    elif type_of_fire == 'Low':
        if 1 <= level_of_the_fire <= 50:
            is_in_range = True
    if is_in_range:
        if water >= level_of_the_fire:
            water-= level_of_the_fire
            effort += level_of_the_fire * 0.25
            total_fire += level_of_the_fire

            print(f"- {level_of_the_fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")