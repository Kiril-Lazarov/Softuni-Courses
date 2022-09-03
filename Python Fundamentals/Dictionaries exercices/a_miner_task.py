def items():
    resource = input()
    item_dict = {}
    while resource != 'stop':
        quantity = int(input())
        if resource not in item_dict:
            item_dict[resource] = quantity
        else:
            item_dict[resource] += quantity
        resource = input()
    for key, value in item_dict.items():
        print(f'{key} -> {value}')


items()
