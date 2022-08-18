stocks = input().split(' ')
dictionary = {}
for i in range(0, len(stocks), 2):
    food = stocks[i]
    quantity = int(stocks[i+1])
    dictionary[food] = quantity
print(dictionary)