def create_force(data, forces_dict):
    side = data[0]
    user = data[1]
    is_user_exist = False
    is_side_exist = False
    for key, value in forces_dict.items():
        number = len(value)
        if side == key:
            is_side_exist = True
        for i in range(number):
            if user == value[i]:
                is_user_exist = True
    if not is_user_exist and not is_side_exist:
        forces_dict[side] = []
        forces_dict[side].append(user)
    elif not is_user_exist and is_side_exist:
        forces_dict[side].append(user)
    return forces_dict


def change_force(data, forces_dict):
    side = data[1]
    user = data[0]
    is_user_exist = False
    is_side_exist = False
    user_current_side = ''
    for key, value in forces_dict.items():
        number = len(value)
        if side == key:
            is_side_exist = True
        for i in range(number):
            if user == value[i]:
                is_user_exist = True
                user_current_side = key
    if not is_user_exist and not is_side_exist:
        forces_dict[side] = []
        forces_dict[side].append(user)
        print(f"{user} joins the {side} side!")
    elif not is_user_exist and is_side_exist:
        forces_dict[side].append(user)
        print(f"{user} joins the {side} side!")
    elif is_user_exist and is_side_exist:
        forces_dict[user_current_side].remove(user)
        if user not in forces_dict[side]:
            forces_dict[side].append(user)
            print(f"{user} joins the {side} side!")
    elif is_user_exist and not is_side_exist:
        forces_dict[side] = [user]
        forces_dict[user_current_side].remove(user)
        print(f"{user} joins the {side} side!")
    return forces_dict


def print_func(forces_dict):
    for key in forces_dict.keys():
        number = len(forces_dict[key])
        if number != 0:
            print(f'Side: {key}, Members: {number}')
            for i in range(number):
                print(f'! {forces_dict[key][i]}')


def force_book():
    forces_dict = {}
    command = input()
    while command != 'Lumpawaroo':
        if '|' in command:
            data = command.split(' | ')
            create_force(data, forces_dict)
        elif '->' in command:
            data = command.split(' -> ')
            change_force(data, forces_dict)
        command = input()
    print_func(forces_dict)


force_book()
