def print_capitals(x):
    # for key, values in x.items():
    #     print(f'{key} -> {values}')
    cubes = {print(f'{key} -> {value}') for (key, value) in x.items() }
def capitals_func():
    countries, capitals = input().split(', '), input().split(', ')
    result = dict(zip(countries, capitals))
    print_capitals(result)

capitals_func()