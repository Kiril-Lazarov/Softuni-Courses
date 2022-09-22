def print_func(x, y):
    for i in range(x):
        searched_name = input()
        if searched_name not in y:
            print(f"Contact {searched_name} does not exist.")
        else:
            print(f"{searched_name} -> {y[searched_name]}")


def phone_book():
    phones_dict = {}
    data = input().split('-')
    while not data[0].isdigit():
        if data[0] not in phones_dict:
            phones_dict[data[0]] = data[1]
        else:
            phones_dict[data[0]] = data[1]
        data = input().split('-')
    number = int(data[0])
    print_func(number, phones_dict)


phone_book()
