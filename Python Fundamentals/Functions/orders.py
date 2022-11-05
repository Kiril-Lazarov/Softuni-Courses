def total_prices(product, quantity):
    result = None
    if product == 'coffee':
        result = 1.5 * quantity
    elif product == 'snacks':
        result = 2 * quantity
    elif product == 'coke':
        result = 1.4 * quantity
    elif product == 'water':
        result = quantity
    return  result


product = input()
quantity = float(input())

print(f'{total_prices(product, quantity):.2f}')