budget = float(input())
season = input()

place = ''
percentage = 1
location = ''

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        percentage = 0.65
    else:
        location = "Morocco"
        percentage = 0.45
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        percentage = 0.8
    else:
        location = "Morocco"
        percentage = 0.6
else:
    place = "Hotel"
    percentage = 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"
print(f"{location} - {place} - {budget * percentage:.2f}")
