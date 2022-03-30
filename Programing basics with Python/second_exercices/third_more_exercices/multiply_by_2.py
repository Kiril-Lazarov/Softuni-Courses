while True:
    number = float(input())
    if number >= 0:
        print(f"Result: {number * 2:.2f}")
        continue
    else:
        print(f"Negative number!")
        break

