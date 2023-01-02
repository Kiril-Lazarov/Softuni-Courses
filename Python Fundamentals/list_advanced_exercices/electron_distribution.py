num_electrons = int(input())
counter = 0
electrons_shells = list()
while True:
    counter += 1
    if num_electrons > 2 * counter ** 2:
        num_electrons -= 2 * counter ** 2
        electrons_shells.append(2 * counter ** 2)
    else:
        electrons_shells.append(num_electrons)
        break
print(electrons_shells)

