# n = int(input())
# heroes_dict = {}
# for i in range(n):
#     command = input().split()
#     heroes_dict[command[0]] = [int(command[1]), int(command[2])]
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     command = command.split(" - ")
#     name = command[1]
#     if command[0] == "CastSpell":
#         mp_needed = int(command[2])
#         spell_name = command[3]
#         if heroes_dict[name][1] >= mp_needed:
#             heroes_dict[name][1] -= mp_needed
#             print(f"{name} has successfully cast {spell_name} and now has {heroes_dict[name][1]} MP!")
#         else:
#             print(f"{name} does not have enough MP to cast {spell_name}!")
#
#     elif command[0] == "TakeDamage":
#         damage = int(command[2])
#         attacker = command[3]
#         heroes_dict[name][0] -= damage
#         if heroes_dict[name][0] <= 0:
#             print(f"{name} has been killed by {attacker}!")
#             del heroes_dict[name]
#         else:
#             print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name][0]} HP left!")
#     elif command[0] == "Recharge":
#         amount = int(command[2])
#         diff = 200 - heroes_dict[name][1]
#         if amount >= diff:
#             heroes_dict[name][1] = 200
#             amount = diff
#         else:
#             heroes_dict[name][1] += amount
#         print(f"{name} recharged for {amount} MP!")
#
#     elif command[0] == "Heal":
#         amount = int(command[2])
#         diff = 100 - heroes_dict[name][0]
#         if amount >= diff:
#             heroes_dict[name][0] = 100
#             amount = diff
#         else:
#             heroes_dict[name][0] += amount
#         print(f"{name} healed for {amount} HP!")
# for key, value in heroes_dict.items():
#     print(f"{key}")
#     print(f"  HP: {value[0]}")
#     print(f"  MP: {value[1]}")
#
#
n = int(input())
heroes = {}
for i in range(n):
    data = input().split(" ")
    heroes[data[0]] = {"HP": int(data[1]), "MP": int(data[2])}
info = input()
while info != "End":
    actions = info.split(" - ")
    if actions[0] == 'CastSpell':
        if heroes[actions[1]]["MP"] >= int(actions[2]):
            heroes[actions[1]]["MP"] -= int(actions[2])
            print(f"{actions[1]} has successfully cast {actions[3]} and now has {heroes[actions[1]]['MP']} MP!")
        else:
            print(f"{actions[1]} does not have enough MP to cast {actions[3]}!")
    elif actions[0] == 'TakeDamage':
        heroes[actions[1]]["HP"] -= int(actions[2])
        if heroes[actions[1]]["HP"] <= 0:
            print(f"{actions[1]} has been killed by {actions[3]}!")
            del heroes[actions[1]]
        else:
            print(
                f"{actions[1]} was hit for {actions[2]} HP by {actions[3]} and now has {heroes[actions[1]]['HP']} HP left!")
    elif actions[0] == 'Recharge':
        diff = int(actions[2])
        if heroes[actions[1]]["MP"] + diff >= 200:
            diff = 200 - heroes[actions[1]]["MP"]
        heroes[actions[1]]["MP"] += diff
        print(f"{actions[1]} recharged for {diff} MP!")
    elif actions[0] == 'Heal':
        diff = int(actions[2])
        if heroes[actions[1]]["HP"] + diff >= 100:
            diff = 100 - heroes[actions[1]]["HP"]
        heroes[actions[1]]["HP"] += diff
        print(f"{actions[1]} healed for {diff} HP!")
    info = input()
for key, value in heroes.items():
    print(f"{key}")
    for item, points in value.items():
        print(f"  {item}: {points}")

