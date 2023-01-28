n = int(input())
rows = []
current = []
cur1 = []
battle_field = []
ships_destroyed = 0
for i in range(n):
    rows = list(map(int, input().split()))
    for j in rows:
        current.append(j)
    battle_field.append(current)
    current = []
attacks = input().split(' ')
for i in attacks:
    row = int(i[0])
    col = int(i[-1])
    if battle_field[row][col] > 0:
        battle_field[row][col] -=1
        if  battle_field[row][col] == 0:
            ships_destroyed +=1
print(ships_destroyed)



