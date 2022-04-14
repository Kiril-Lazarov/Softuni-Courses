age = float(input())
gender = input()
appeal = ""
if age < 16:
    if gender == "m":
        appeal = "Master"
    elif gender == "f":
        appeal = "Miss"
elif age >= 16:
    if gender == "m":
        appeal = "Mr."
    elif gender == "f":
        appeal = "Ms."
print(appeal)