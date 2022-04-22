budget = float(input())
season = input()
place = ''
destination = ''
total_sum = 0
if budget <= 100:
    if season == 'summer':
        total_sum = budget * 0.3
        destination = 'Bulgaria'
        place = 'Camp'
    elif season == 'winter':
        total_sum = budget * 0.7
        destination = 'Bulgaria'
        place = 'Hotel'
elif budget <= 1000:
    if season == 'summer':
        total_sum = budget * 0.4
        destination = 'Balkans'
        place = 'Camp'
    elif season == 'winter':
        total_sum = budget * 0.8
        destination = 'Balkans'
        place = 'Hotel'
else:
    total_sum = budget * 0.9
    destination = 'Europe'
    if season == 'summer':
        place = 'Hotel'
    elif season == 'winter':
        place = 'Hotel'
print(f"Somewhere in {destination}")
print(f"{place} - {total_sum:.2f}")
