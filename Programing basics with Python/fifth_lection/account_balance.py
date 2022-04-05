money = input()

total_sum = 0
while money != "NoMoreMoney":
    if float(money) >= 0:
        total_sum += float(money)
        print(f"Increase: {float(money):.2f}")
        money = input()
    else:
        print("Invalid operation!")
        break
print(f"Total: {total_sum:.2f}")
