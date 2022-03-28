radius = float(input())

from math import pi

perimeter_circle = 2 * pi * radius
surface_circle = pi * radius * radius

print(f'{surface_circle:.2f}')
print(f'{perimeter_circle:.2f}')