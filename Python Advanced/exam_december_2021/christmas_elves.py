from collections import deque

elfs = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_elf_energy = 0
total_toys = 0
turn = 0
while True:
    turn += 1
    curr_elf = elfs[0]
    energy_to_spent = materials[-1]
    cookie = 1
    toys_to_created = 1
    if curr_elf < 5:
        elfs.popleft()
        turn -= 1
        if not elfs:
            break
        else:
            continue
    if turn % 3 == 0:
        toys_to_created = 2
        energy_to_spent *= 2
    if turn % 5 == 0:
        toys_to_created = 0
        cookie = 0
    if curr_elf >= energy_to_spent:
        total_toys += toys_to_created
        total_elf_energy += energy_to_spent
        elfs[0] = (curr_elf- energy_to_spent + cookie)
        elfs.append(elfs.popleft())
        materials.pop()
        if not materials:
            break
    else:
        elfs[0] = curr_elf*2
        elfs.append(elfs.popleft())


print(f'Toys: {total_toys}')
print(f'Energy: {total_elf_energy}')
if elfs:
    print(f"Elves left: {', '.join([str(x) for x in elfs])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")

