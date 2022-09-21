def orders():
    stocks_dict = {}
    products = input().split(' ')
    while products[0] != 'buy':
        product = products[0]
        price = float(products[1])
        quantity = int(products[2])
        if products[0] not in stocks_dict:
            stocks_dict[products[0]] = [price, quantity]

        else:
            stocks_dict[products[0]] = [price, (quantity + stocks_dict[products[0]][1])]

        products = input().split(' ')
    for key, value in stocks_dict.items():
        print(f'{key} -> {value[0]*value[1]:.2f}')


orders()
