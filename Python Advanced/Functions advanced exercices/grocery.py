def grocery_store(**kwargs):
    list = []
    result  = {k:v for k,v in sorted(kwargs.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))}
    for key, value in result.items():
        list.append(f'{key}: {value}')
    return '\n'.join(list)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
