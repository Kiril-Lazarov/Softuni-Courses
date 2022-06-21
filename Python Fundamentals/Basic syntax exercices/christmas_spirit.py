# •	Ornament Set – 2$ per piece
# •	Tree Skirt – 5$ per piece
# •	Tree Garlands – 3$ per piece
# •	Tree Lights – 15$ per piece
# •	quantity – integer in the range [1…100]
# •	days – integer in the range [1…100]

quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
christmas_spirit = 0
budget = 0
for i in range(1, days +1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += ornament_set * quantity
        christmas_spirit += 5
    if i % 3 == 0:
        budget += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
    if i % 5 == 0:
        budget += tree_lights * quantity
        christmas_spirit += 17
    if i % 10 == 0:
        budget += tree_skirt + tree_garlands + tree_lights
        christmas_spirit -= 20

    if i % 15 == 0:
        christmas_spirit += 30
if days % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")


