day_of_week = input(" ")

type_day = " "

if day_of_week == "Monday" \
    or day_of_week == "Tuesday"\
    or day_of_week == "Wednesday"\
    or day_of_week == "Thursday"\
    or day_of_week == "Friday":
    type_day = "Working day"
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    type_day = "Weekend"
else:
    type_day = "Error"
print(type_day)