events = input().split('|')
events_list = list()
initial_energy = 100
initial_coins = 100
isClosed = False
for i in range(len(events)):

    events_list = events[i].split('-')
    type_event = events_list[0]
    number = int(events_list[-1])
    if type_event == "rest":
        if initial_energy == 100:
            gained_energy = 100 - initial_energy
        else:
            gained_energy = number
            initial_energy += number
            if initial_energy >= 100:
                initial_energy = 100
                gained_energy = initial_energy -100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif type_event == "order":

        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50

            print("You had to rest!")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {type_event}.")
        else:
            print(f"Closed! Cannot afford {type_event}.")
            isClosed = True
            break

if isClosed == False:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")