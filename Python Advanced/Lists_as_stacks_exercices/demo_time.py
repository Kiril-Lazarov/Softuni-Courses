seconds = 86400

hours = seconds // 3600
hours_remainder = seconds % 3600
if hours >= 24:
    hours %= 24
minutes = hours_remainder // 60
minutes_remainder = hours_remainder % 60

if hours <10:
    hours = f'{0}{hours}'
if minutes< 10:
    minutes = f'{0}{minutes}'
if minutes_remainder< 10:
    minutes_remainder = f'{0}{minutes_remainder}'
print(f'{hours}:{minutes}:{minutes_remainder}')
