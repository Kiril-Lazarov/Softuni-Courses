from math import floor, ceil

magnolia_price = int(input())
hyacinth_price = int(input())
rose_price = int(input())
cactus_price = int(input())
gift_price = float(input())

order_sum = (magnolia_price * 3.25 + hyacinth_price * 4 + rose_price * 3.50 + cactus_price * 8) * 0.95

if order_sum >= gift_price:
    print(f"She is left with {floor(order_sum - gift_price)} leva." )
else:
    print(f"She will have to borrow {ceil(gift_price - order_sum)} leva.")