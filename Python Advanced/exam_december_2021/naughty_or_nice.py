def naughty_or_nice_list(names,*args, **kwargs):
    number_name_counter = 0
    matched_name = ''
    kids = {'Nice': [], 'Naughty': [], 'Not found': []}
    commands = args
    santa_list = []
    for command in commands:
        number, type = command.split('-')
        number = int(number)
        for num, kid_name in names:
            if number == num:
                number_name_counter += 1
                matched_name = kid_name
        if number_name_counter == 1:
            names.remove((number, matched_name))
            kids[type].append(matched_name)
        number_name_counter = 0
        matched_name = ''
    if kwargs:
        for name, type in kwargs.items():
            number = 0
            for num, kid_name in names:
                if name == kid_name:
                    number_name_counter += 1
                    matched_name = kid_name
                    number = num
            if number_name_counter == 1:
                names.remove((number, matched_name))
                kids[type].append(matched_name)
            number_name_counter = 0
            matched_name = ''
    if names:
        for num, kid_name in names:
            kids['Not found'].append(kid_name)
    print_list = []
    for type, names in kids.items():
        if names:
            print_list.append(f'{type}: {", ".join(names)}')

    return '\n'.join(print_list)






    # print(nums)
    # print(sorted_kids)
    # # print(commands)
    # # print(kwargs)
    #
    # for command in commands:
    #     num = int(command.split('-')[0])
    #     type = command.split('-')[1]
    #     counter = 0
    #
    #     idx = 0
    #     for kid in santa_list:
    #         if num == kid[0]:
    #             counter += 1
    #             idx = santa_list.index(kid)
    #
    #     if counter == 1:
    #
    #         number, name = santa_list[idx]
    #
    #         # idx = santa_list.index((number, name))
    #         if type == 'Naughty':
    #             kids['Naughty'].append(name)
    #             del santa_list[santa_list.index((number, name))]
    #         elif type == "Nice":
    #             kids['Nice'].append(name)
    #             del santa_list[idx]
    # for pair in santa_list:
    #     number, name = pair
    #     final_list.append(name)
    # if kwargs:
    #     for key, value in kwargs.items():
    #         if value == 'Naughty':
    #             if key not in kids['Nice']:
    #                 kids['Naughty'].append(key)
    #                 del final_list[final_list.index(key)]
    #         elif value == 'Nice':
    #
    #             if key not in kids['Naughty']:
    #                 kids['Nice'].append(key)
    #                 del final_list[final_list.index(key)]
    # if final_list:
    #     kids['Not found'] = final_list
    # else:
    #     del kids['Not found']
    #
    # print_list = []
    # for type, names in kids.items():
    #     if names:
    #         print_list.append(f'{type}: {", ".join(names)}')
    #
    # return '\n'.join(print_list)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
