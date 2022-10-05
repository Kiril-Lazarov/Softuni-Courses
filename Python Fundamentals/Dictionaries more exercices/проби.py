# names = []
# colors = []
# points = []
# for i in range(3):
#     text = input()
#     if i == 0:
#         names.append(text)
#     elif i == 1:
#         colors.append(text)
#     else:
#         points.append(text)
#
# my_dict = dict(zip(colors, names))
# my_dict = dict(zip(my_dict, points))
# print(my_dict)
# Peter <:> Red <:> 2000
# Teodor <:> Blue <:> 1000
# George <:> Blue <:> 1000
# Simon <:> Yellow <:> 4500
# Dopey <:> Blue <:> 1000
# Peter <:> Blue <:> 3000
# Teodor <:> Blue <:> 1000
# George <:> Yellow <:> 3000
# Peter <:> Red <:> 3000
# Qvor <:> Yellow <:> 3000
# George <:> Yellow <:> 4500
# Simon <:> Yellow <:> 5000
# Aatti <:> Yellow <:> 3000
# Ammi <:> Yellow <:> 3000
# George <:> Yellow <:> 4500
# Simon <:> Yellow <:> 5000
# Once upon a time
from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7]

print(reduce(lambda x,y: x*y, a))