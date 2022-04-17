item = input()
town = input()
quantity = float(input())
price = 0

if item == "coffee":
    if town == "Sofia":
        price = 0.5
    elif town == "Plovdiv":
        price = 0.4
    elif town == "Varna":
        price = 0.45
elif item == "water":
    if town == "Sofia":
        price = 0.8
    elif town == "Plovdiv":
        price = 0.7
    elif town == "Varna":
        price = 0.7
elif item == "beer":
    if town == "Sofia":
        price = 1.2
    elif town == "Plovdiv":
        price = 1.15
    elif town == "Varna":
        price = 1.1
elif item == "sweets":
    if town == "Sofia":
        price = 1.45
    elif town == "Plovdiv":
        price = 1.3
    elif town == "Varna":
        price = 1.35
elif item == "peanuts":
    if town == "Sofia":
        price = 1.6
    elif town == "Plovdiv":
        price = 1.5
    elif town == "Varna":
        price = 1.55
price *= quantity
print(price)

