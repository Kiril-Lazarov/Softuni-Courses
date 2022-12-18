to_do_list = input()
priority_list = ['' for i in range(11)]

while to_do_list != 'End':
    instructions = to_do_list.split('-')
    index = int(instructions[0])
    action = instructions[1]
    priority_list[index] = action

    to_do_list = input()
priority_list = [i for i in priority_list if i != '']
print(priority_list)