dwarf_dict = {}
while True:
    data = input()
    if data == 'Once upon a time':
        break
    name, colour, physics = data.split(' <:> ')
    if name not in dwarf_dict.keys():
        dwarf_dict[name] = {colour: int(physics)}
    else:
        if colour in dwarf_dict[name].keys():
            dwarf_dict[name][colour] = max(dwarf_dict[name].get(colour, 0), int(physics))
        else:
            dwarf_dict[name][colour] = int(physics)
list = []
points_dict = {}
for name in dwarf_dict:
    for colour, points in dwarf_dict[name].items():
        list.append([points, colour, name])
for i in list:
    if i[0] not in points_dict.keys():
        if len(points_dict) == 0:
            points_dict = {i[0]: {i[1]: [i[2]]}}
        else:
            points_dict[i[0]] = {i[1]: [i[2]]}
    else:
        if i[1] not in points_dict[i[0]]:
            points_dict[i[0]][i[1]] = [i[2]]
        else:
            points_dict[i[0]][i[1]].append(i[2])
points_dict = {k: v for k, v in sorted(points_dict.items(), reverse=True)}  # reverse by points
for key, value in points_dict.items():
    for keys, values in points_dict[key].items():
        points_dict[key] = {k: v for k, v in sorted(points_dict[key].items(), key=lambda x: len(x[1]),
                                                    reverse=True)}  # sort by lenght of color
        points_dict[key][keys] = sorted(values)

for points, value in points_dict.items():
    for colour, name in value.items():
        for i in name:
            print(f"({colour}) {i} <-> {points}")
