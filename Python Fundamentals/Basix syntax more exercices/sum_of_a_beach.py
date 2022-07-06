# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words
# "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
list1 = []
string = input()
water = ['W', 'A', 'T', 'E', 'R']
fish = ['F', 'I', 'S', 'H']
sun = ['S', 'U', 'N']
sand = ['S', 'A', 'N', 'D']

water_counter = 0
fish_counter = 0
sun_counter = 0
sand_counter = 0

for i in range(len(string)):
    list1.append(string[i].upper())
for j in range(len(list1) + 1):
    if water == list1[j:j + 5]:
        water_counter += 1

for j in range(len(list1) + 1):
    if fish == list1[j:j + 4]:
        fish_counter += 1

for j in range(len(list1) + 1):
    if sun == list1[j:j + 3]:
        sun_counter += 1

for j in range(len(list1) + 1):
    if sand == list1[j:j + 4]:
        sand_counter += 1
result = water_counter + fish_counter + sun_counter + sand_counter
print(result)
