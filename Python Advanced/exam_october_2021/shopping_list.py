def shopping_list(budget, **kwargs):
    types = {}
    if budget< 100:
        return 'You do not have enough budget.'
    else:
        for key, value in kwargs.items():
            if len(types)<5:
                total = value[0] * value[1]
                if total <=budget:
                    types[key] = total
                    budget -= total



    final_list = []
    for key, value in types.items():
        final_list.append(f'You bought {key} for {value:.2f} leva.')
    return ('\n'.join(final_list))



print(shopping_list(100,microwave=(70, 2),skirts=(15, 4),coffee=(1.50, 10),))
print(shopping_list(20,jeans=(19.99, 1),))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


