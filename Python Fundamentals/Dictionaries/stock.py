stocks = input().split(' ')
items = input().split(' ')
dictionary = {}
for i in range(0, len(stocks), 2):
    food = stocks[i]
    quantity = int(stocks[i + 1])
    dictionary[food] = quantity
for i in items:

    if i in dictionary.keys():
        print(f"We have {dictionary[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")

