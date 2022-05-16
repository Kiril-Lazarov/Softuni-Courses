command = input()

while command != 'End':
    place = command
    needed_money = float(input())
    while needed_money > 0:
        saved_money = float(input())
        needed_money -= saved_money

    print(f"Going to {place}!")
    command = input()
