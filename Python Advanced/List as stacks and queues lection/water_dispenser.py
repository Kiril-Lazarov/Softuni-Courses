from collections import deque
people = deque()

start_litters = int(input())

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        break
    elif command.startswith("refill "):
        command = command.split(" ")
        quantity = int(command[1])
        start_litters += quantity
    else:
        quantity = int(command)
        name = people.popleft()
        if quantity <= start_litters:
            print(f"{name} got water")
            start_litters -= quantity
        else:
            print(f'{name} must wait')
print(f'{start_litters} liters left')

