example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}


def start_spring(**kwargs):
    count_dict = {}
    for key, value in kwargs.items():
        if value not in count_dict:
            count_dict[value] = []
        count_dict[value].append(key)
    count_dict = {k:v for k,v in sorted(count_dict.items(), key= lambda x:(-len(x[1]), x[0]))}

    print_list = []
    for key, value in count_dict.items():
        value = sorted(value)
        print_list.append(f'{key}:')
        for item in value:
            print_list.append(f'-{item}')

    return '\n'.join(print_list)
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
