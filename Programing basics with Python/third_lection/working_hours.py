hour = int(input())
day_of_week = input()
result = ""

if 10 <= hour <= 18 and day_of_week != "Sunday":
    result = "open"
else:
    result = "closed"
print(result)
