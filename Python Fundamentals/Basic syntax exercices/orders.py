N = int(input())
total_price = 0
for i in range(N):
    price = float(input())
    days = int(input())
    capsules = int(input())
    sum_price = price * days * capsules
    total_price += sum_price
    print(f"The price for the coffee is: ${sum_price:.2f}")
print(f"Total: ${total_price:.2f}")
