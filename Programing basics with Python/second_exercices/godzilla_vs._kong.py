

budget = float(input())
statists_count = int(input())
wear_price_per_statist = float(input())
discount = 0
dekor = budget * 0.1


if statists_count > 150:
    discount = 0.9
    total_cost = statists_count * wear_price_per_statist * discount + dekor
    final_sum = budget - total_cost
    if final_sum >= 0:
        print("Action!")
        print(f"Wingard starts filming with {final_sum:.2f} leva left.")
    else:
        print("Not enough money!")
        print(f"Wingard needs {final_sum * (-1):.2f} leva more.")
else:
    total_cost = statists_count * wear_price_per_statist + dekor
    final_sum = budget - total_cost
    if final_sum >= 0:
        print("Action!")
        print(f"Wingard starts filming with {final_sum:.2f} leva left.")
    else:
        print("Not enough money!")
        print(f"Wingard needs {final_sum * (-1):.2f} leva more.")


