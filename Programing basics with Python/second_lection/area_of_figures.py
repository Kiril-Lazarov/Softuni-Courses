from math import pi

type_of_the_figure = input()
result = 0

if type_of_the_figure == "square":
    side = float(input())
    result = side * side

elif type_of_the_figure == "rectangle":
    side = float(input())
    side_b = float(input())
    result = side * side_b

elif type_of_the_figure == "circle":
    radius = float(input())
    result = radius * pi * radius
else:
    side = float(input())
    high = float(input())
    result = side * high / 2
print(f'{result:.3f}')
