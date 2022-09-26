def sort_dragons(dragons_dict):
    for key, value in dragons_dict.items():
        data_list = []
        value = {k: v for k, v in sorted(value.items(), key=lambda x: x[0])}
        for num in value.values():
            data_list.append(num)
        result = [f'{sum(x) / len(x):.2f}' for x in zip(*data_list)]
        print(f"{key}::({result[0]}/{result[1]}/{result[2]})")
        for name, points in value.items():
            print(f"-{name} -> damage: {points[0]}, health: {points[1]}, armor: {points[2]}")


def dragons_inputs():
    n = int(input())
    default_values = [45, 250, 10]
    dragons_dict = {}
    for i in range(n):
        colour, name, damage, health, armour = input().split()
        if colour not in dragons_dict.keys():
            dragons_dict[colour] = {name: [damage, health, armour]}
        else:
            dragons_dict[colour][name] = [damage, health, armour]
        for colour, name in dragons_dict.items():
            for key, values in name.items():
                for j in range(3):
                    if values[j] == 'null':
                        values[j] = default_values[j]
                    else:
                        values[j] = int(values[j])
    sort_dragons(dragons_dict)


dragons_inputs()
