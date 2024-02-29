from collections import  deque
counter = 0
elements = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

bomb_dict = {'Cherry Bombs': 0, 'Datura Bombs': 0, 'Smoke Decoy Bombs': 0}
bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casing = deque([int(x) for x in input().split(', ')])

while bomb_casing and bomb_effects:
    bomb_eff = bomb_effects[0]
    bomb_cas = bomb_casing[-1]
    mix = bomb_cas + bomb_eff
    if mix in elements:
        bomb_dict[elements[mix]] +=1
        bomb_effects.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5
    counter = 0
    for num in bomb_dict.values():
        if num >= 3:
            counter +=1
    if counter == 3:
        break




if counter >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    # bomb_effects = sorted([str(x) for x in bomb_effects], reverse= True)
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effects)}')
else:
    print("Bomb Effects: empty")
if bomb_casing:
    # bomb_casing = sorted([str(x) for x in bomb_casing], reverse= True)
    print(f'Bomb Casings: {", ".join(str(x) for x in bomb_casing)}')
else:
    print("Bomb Casings: empty")
for key, value in bomb_dict.items():
    print(f'{key}: {value}')