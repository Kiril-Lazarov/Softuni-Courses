# n = int(input())
# mobiles = {}
#
# for i in range(n):
#     command = input().split('|')
#     mobiles[command[0]] = [int(command[1]), int(command[2])]
#
# while True:
#     command = input()
#     if command == 'Stop':
#         break
#     command = command.split(' : ')
#     car = command[1]
#     if command[0] == "Drive":
#         distance = int(command[2])
#         fuel = int(command[3])
#         if mobiles[car][1] >= fuel:
#             mobiles[car][1] -= fuel
#             mobiles[car][0] += distance
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#         else:
#             print(f"Not enough fuel to make that ride")
#         if mobiles[car][0] >= 100000:
#             print(f"Time to sell the {car}!")
#             del mobiles[car]
#
#     elif command[0] == "Refuel":
#         fuel = int(command[2])
#         diff = 75 - mobiles[car][1]
#         if fuel >= diff:
#             mobiles[car][1] = 75
#             fuel = diff
#         else:
#             mobiles[car][1] += fuel
#         print(f"{car} refueled with {fuel} liters")
#     elif command[0] == "Revert":
#         kilometers = int(command[2])
#         mobiles[car][0] -= kilometers
#         if mobiles[car][0] < 10000:
#             mobiles[car][0] = 10000
#         else:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#
# for key, value in mobiles.items():
#     print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
n = int(input())
cars = {}
for i in range(n):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}

info = input()
while info != "Stop":
    data = info.split(" : ")
    if data[0] == 'Drive':
        if cars[data[1]]["fuel"] < int(data[3]):
            print("Not enough fuel to make that ride")
        else:
            cars[data[1]]['mileage'] += int(data[2])
            cars[data[1]]["fuel"] -= int(data[3])
            print(f"{data[1]} driven for {data[2]} kilometers. {data[3]} liters of fuel consumed.")
            if cars[data[1]]['mileage'] >= 100000:
                print(f"Time to sell the {data[1]}!")
                del cars[data[1]]
    elif data[0] == 'Refuel':
        diff = int(data[2])
        if cars[data[1]]["fuel"] + diff <= 75:
            cars[data[1]]["fuel"] += diff
        else:
            diff = 75 - cars[data[1]]["fuel"]
            cars[data[1]]["fuel"] = 75
        print(f"{data[1]} refueled with {diff} liters")

    elif data[0] == 'Revert':
        if cars[data[1]]['mileage'] - int(data[2]) >= 10000:
            cars[data[1]]['mileage'] -= int(data[2])
            print(f"{data[1]} mileage decreased by {data[2]} kilometers")
        else:
            cars[data[1]]['mileage'] = 10000
    info = input()
for key, values in cars.items():
    data = []
    for k, v in values.items():
        data.append(v)
    print(f"{key} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")


