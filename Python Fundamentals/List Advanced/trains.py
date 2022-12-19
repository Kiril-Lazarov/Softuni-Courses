n = int(input())
wagons = [0 for i in range(n)]
command = input()

while command != 'End':
    instruction = command.split(' ')
    action = instruction[0]
    if action == 'add':
        wagons[-1] +=int(instruction[1])
    elif action == 'insert':
        index = int(instruction[1])
        people = int(instruction[2])
        wagons[index] += people
    elif action == 'leave':
        index = int(instruction[1])
        people = int(instruction[2])
        wagons[index] -= people
    command = input()
print(wagons)