fuel_type = input()
available_liters = float(input())

if fuel_type == "Diesel":
    if available_liters >= 25:
        print("You have enough diesel.")
    else:
        print("Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if available_liters >= 25:
        print("You have enough gasoline.")
    else:
        print("Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if available_liters >= 25:
        print("You have enough gas.")
    else:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")