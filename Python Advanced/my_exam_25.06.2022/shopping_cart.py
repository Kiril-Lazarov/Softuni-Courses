def shopping_cart(*args):
    carts = {'Soup':[],'Pizza':[],'Dessert':[]}
    for item in args:
        if item == 'Stop':

            break
        else:
           type = item[0]
           product = item[-1]
           if type == 'Soup':
               if len(carts['Soup']) <3 and product not in carts['Soup']:
                   carts['Soup'].append(product)

           elif type == 'Pizza':
               if len(carts['Pizza']) <4 and product not in carts['Pizza']:
                   carts['Pizza'].append(product)
           elif type == 'Dessert':
               if len(carts['Dessert']) < 2 and product not in carts['Dessert']:
                   carts['Dessert'].append(product)
    number = 0
    for key, value in carts.items():
        if not value:
            number +=1
        if number == 3:
            return  "No products in the cart!"
    for key, value in carts.items():
        carts[key] = sorted(value)
    sorted_carts = {k:v for k, v in sorted(carts.items(), key= lambda x: (-len(x[1]), x[0]))}
    final_list = []
    for key, value in sorted_carts.items():
        final_list.append(f'{key}:')
        for product in value:
            final_list.append(f" - {product}")


    return '\n'.join(final_list)







print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


