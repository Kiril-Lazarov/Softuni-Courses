change = float(input())
# coin1 = 1
# coin2 = 2
# coin01 = 0.1
# coin02 = 0.2
# coin05 = 0.5
# coin001 = 0.01
# coin002 = 0.02
# coin005 = 0.05

total_coins = 0
current_change = change
while change > 0:
    if change // 2 > 0:
        total_coins += change // 2
        change = round(change % 2, 2)

    elif change // 1 > 0:
        total_coins += change // 1
        change = round(change % 1, 2)

    elif change // 0.5 > 0:
        total_coins += change // 0.5
        change = round(change % 0.5, 2)

    elif change // 0.2 > 0:
        total_coins += change // 0.2
        change = round(change % 0.2, 2)

    elif change // 0.1 > 0:
        total_coins += change // 0.1
        change = round(change % 0.1, 2)

    elif change // 0.05 > 0:
        total_coins += change // 0.05
        change = round(change % 0.05, 2)

    elif change // 0.02 > 0:
        total_coins += change // 0.02
        change = round(change % 0.02, 2)

    elif change // 0.01 > 0:
        total_coins += change // 0.01
        change = round(change % 0.01, 2)

print(f'{total_coins:.0f}')
