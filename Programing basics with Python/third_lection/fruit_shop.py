fruit = input()
day_of_week = input()
quantity = float(input())
working_day = 0
price = 0
is_fruit = True
if day_of_week == "Monday" \
     or day_of_week == "Tuesday" \
     or day_of_week == "Wednesday" \
     or day_of_week == "Tuesday" \
     or day_of_week == "Friday":
    working_day = 1
elif day_of_week == "Saturday"\
     or day_of_week == "Sunday":
    working_day = 2
else:
    working_day = working_day
if fruit == "banana":
    if working_day == 1:
        price = 2.5
    elif working_day == 2:
        price = 2.7
elif fruit == "apple":
    if working_day == 1:
        price = 1.2
    elif working_day == 2:
        price = 1.25
elif fruit == "orange":
    if working_day == 1:
        price = 0.85
    elif working_day == 2:
        price = 0.9
elif fruit == "grapefruit":
    if working_day == 1:
        price = 1.45
    elif working_day == 2:
        price = 1.6
elif fruit == "kiwi":
    if working_day == 1:
        price = 2.7
    elif working_day == 2:
        price = 3
elif fruit == "pineapple":
    if working_day == 1:
        price = 5.5
    elif working_day == 2:
        price = 5.6
elif fruit == "grapes":
    if working_day == 1:
        price = 3.85
    elif working_day == 2:
        price = 4.2
else:
    is_fruit = False
if is_fruit != True or working_day == 0:
    print("error")
else:
    print(f"{price * quantity:.2f}")


# print(is_fruit)

