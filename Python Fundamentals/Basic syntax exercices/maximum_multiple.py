# divisor = int(input())
# boundary = int(input())
# print(max([i for i in range(2, boundary+1) if i % divisor == 0]) )

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
# for member in planets:
#     for planet in member:
#         if len(planet)<6:
#             final.append(planet)

final = [planet for member  in planets for planet  in member if len(planet)<6 ]
print(final)