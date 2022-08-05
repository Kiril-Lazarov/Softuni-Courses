losts = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_costs = 0
shield_counter = 0
for i in range(1, losts+1):
    if i % 2 == 0:
        total_costs += helmet_price
    if i % 3== 0:
        total_costs += sword_price
    if i % 6 == 0:
        total_costs += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            total_costs += armor_price
print(f"Gladiator expenses: {total_costs:.2f} aureus")