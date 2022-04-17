city = input()
sales = float(input())
commission = 0

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.1
    elif city == "Plovdiv":
        commission = 0.12
elif sales > 10000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
else:
    commission = commission
if commission != 0:
    total = sales * commission
    print(f'{total:.2f}')
else:
    print("error")
