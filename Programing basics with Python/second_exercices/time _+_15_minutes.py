hour = int(input())
minutes = int(input())
total_hour = 0
total_minutes = 0

if (minutes + 15) >= 60:
    total_hour = hour + 1
    total_minutes = (minutes + 15) % 60
    if total_hour >=24:
        if total_minutes < 10:
            print(f'0:0{total_minutes}')
        else:
            print(f'0:{total_minutes}')
    elif total_hour < 24:
        if total_minutes < 10:
            print(f'{total_hour}:0{total_minutes}')
        else:
            print(f'{total_hour}:{total_minutes}')
    else:
        print(f'{total_hour}:{total_minutes}')
else:
    print(f'{hour}:{minutes + 15}')
