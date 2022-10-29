# cities_dict = {}
# while True:
#     command = input()
#     if command == "Sail":
#         break
#     command = command.split('||')
#     sity , population, gold = command[0], int(command[1]), int(command[2])
#     if sity in cities_dict:
#         cities_dict[sity][0] += population
#         cities_dict[sity][1] += gold
#     else:
#         cities_dict[sity] = [population, gold]
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     command = command.split('=>')
#     if command[0] == "Plunder":
#         town, people, gold = command[1], int(command[2]), int(command[3])
#         cities_dict[town][0] -= people
#         cities_dict[town][1] -= gold
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#         if cities_dict[town][0] <= 0 or cities_dict[town][1] <= 0:
#             del cities_dict[town]
#             print(f"{town} has been wiped off the map!")
#     elif command[0] == "Prosper":
#         town,gold = command[1], int(command[2])
#         if gold >= 0:
#             cities_dict[town][1] += gold
#             print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.")
#         else:
#             print("Gold added cannot be a negative number!" )
# number = len(cities_dict)
# if number != 0:
#     print(f"Ahoy, Captain! There are {number} wealthy settlements to go to:")
#     for key, value in cities_dict.items():
#         print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")
#
cities = {}
while True:
    data = input()
    if data == "Sail":
        break
    info = data.split("||")
    if info[0] not in cities:
        cities[info[0]] = {"Population": int(info[1]), "Gold": int(info[2])}
    else:
        cities[info[0]]["Population"] += int(info[1])
        cities[info[0]]["Gold"] += int(info[2])
while True:
    data = input()
    if data == "End":
        break
    info = data.split("=>")
    town = info[1]
    gold = int(info[-1])
    if info[0] == 'Plunder':
        people = int(info[2])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["Population"] -= people
        cities[town]["Gold"] -= gold
        if cities[town]["Population"] <= 0 or cities[town]["Gold"] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif info[0] == 'Prosper':
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['Gold']} gold.")
if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities:
        print(f"{town} -> Population: {cities[town]['Population']} citizens, Gold: {cities[town]['Gold']} kg")
