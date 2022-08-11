number_lines = int(input())
capacity = 255
fill = 0
isEmpty = True

for i in range(number_lines):
    litters = int(input())
    if litters <= capacity:
        capacity -= litters
        fill += litters
    else:
        print("Insufficient capacity!" )
print(fill)
