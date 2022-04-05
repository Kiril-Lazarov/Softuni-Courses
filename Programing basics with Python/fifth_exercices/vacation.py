needed_money = float(input())
available_money = float(input())

days = 0
days_of_spend = 0
last_action = ''

while True:
    action = input()
    action_sum = float(input())
    days += 1
    last_action = action

    if action == "save":
        available_money += action_sum
    else:
        available_money -= action_sum

    if available_money <= 0:
        available_money = 0
    if last_action == "spend":
        days_of_spend += 1
    else:
        days_of_spend = 0

    if days_of_spend == 5:
        print("You can't save the money.")
        print(days)
        break
        
    if available_money >= needed_money:
        print(f"You saved the money for {days} days.")
        break

