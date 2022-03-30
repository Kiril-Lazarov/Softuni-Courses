time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
seconds_to_minutes_convertor = total_time // 60
total_time_reminder_in_seconds = total_time % 60

if total_time_reminder_in_seconds < 10:
    print(f'{seconds_to_minutes_convertor}:0{total_time_reminder_in_seconds}')
else:
    print(f'{seconds_to_minutes_convertor}:{total_time_reminder_in_seconds}')

