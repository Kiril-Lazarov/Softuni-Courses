from collections import deque

waiting_cars = deque()

is_crashed = False
passing_cars_list = []
# curr_car = deque()

green_light = int(input())
free_window = int(input())


def go():
    global hit_letter

    curr_car = waiting_cars.popleft()
    passing_cars_list.append(curr_car)
    curr_car = deque([x for x in curr_car])

    for i in range(green_light):

        if not curr_car and waiting_cars:
            if i <= green_light -1:
                curr_car = waiting_cars.popleft()
                passing_cars_list.append(curr_car)
                curr_car = deque([x for x in curr_car])
                curr_car.popleft()

        elif not curr_car and not waiting_cars:
            return False
        elif curr_car:
            curr_car.popleft()

    if curr_car:
        if free_window >= len(curr_car):
            return False
        else:
            hit_letter = curr_car[free_window]
            return True


hit_letter = ''
while True:
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        if waiting_cars:
            if go():
                break
    else:
        waiting_cars.append(command)

if hit_letter:
    print("A crash happened!")
    print(f"{passing_cars_list[-1]} was hit at {hit_letter}.")
else:
    print(f'Everyone is safe.')
    print(f'{len(passing_cars_list)} total cars passed the crossroads.')
