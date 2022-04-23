# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

hour_examination = int(input())
minute_examination = int(input())
arrival_hour = int(input())
minute_arrival = int(input())

time_exam = f'{hour_examination}:{minute_examination}'
time_arrival = f'{arrival_hour}:{minute_arrival}'
status = ''
difference = (hour_examination * 60 + minute_examination) - (arrival_hour * 60 + minute_arrival)
minutes_difference = 0
hours_difference = 0
expression1 = ''
expression2 = ''


if difference == 0:
    status = 'On time'
elif difference > 0:
    if difference <= 30:
        status = 'On time'
    else:
        status = 'Early'
    if 0 < difference < 60:
        minutes_difference = difference
        expression1 = "minutes"
        expression2 = 'before the start'

    elif difference >= 60:
        minutes_difference = difference % 60
        hours_difference = difference // 60
        expression1 = 'hours'
        expression2 = 'before the start'

else:
    status = 'Late'
    if -60 < difference < 0:
        minutes_difference = abs(difference)
        expression1 = "minutes"
        expression2 = 'after the start'

    elif difference <= -60:
        minutes_difference = abs(difference) % 60
        hours_difference = abs(difference) // 60
        expression1 = 'hours'
        expression2 = 'after the start'
print(status)
if minutes_difference < 10:
    print(f'{hours_difference}:0{minutes_difference} {expression1} {expression2}')
    if hours_difference == 0:
        print(f'0{minutes_difference} {expression1} {expression2}')
else:
    if hours_difference == 0:
        print(f'{minutes_difference} {expression1} {expression2}')
    else:
        print(f'{hours_difference}:{minutes_difference} {expression1} {expression2}')















































# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

# hour_examination = int(input())
# minute_examination = int(input())
# arrival_hour = int (input())
# minute_arrival = int(input())
#
# time_exam = f'{hour_examination}:{minute_examination}'
# time_arrival = f'{arrival_hour}:{minute_arrival}'
# status = ''
# difference = (hour_examination * 60 + minute_examination) - (arrival_hour * 60 + minute_arrival)
# minutes_difference = 0
# hours_difference = 0
#
# if difference == 0:
#     status = 'On time'
#     print(status)
#
# elif difference > 0:
#     if difference <= 30:
#         status = 'On time'
#     else:
#         status = 'Early'
#     if 0 < difference < 60:
#         minutes_difference = difference
#         print(status)
#         print(f'{minutes_difference} minutes before the start')
#     elif difference >= 60:
#         minutes_difference = difference % 60
#         hours_difference = difference // 60
#         print(status)
#         if minutes_difference < 10:
#             print(f'{hours_difference}:0{minutes_difference} hours before the start')
#         else:
#             print(f'{hours_difference}:{minutes_difference} hours before the start')
# else:
#     status = 'Late'
#     if -60 < difference < 0:
#         minutes_difference = abs(difference)
#         print(status)
#         print(f'{minutes_difference} minutes after the start')
#     elif difference <= -60:
#         minutes_difference = abs(difference) % 60
#         hours_difference = abs(difference) // 60
#         print(status)
#         if minutes_difference < 10:
#             print(f'{hours_difference}:0{minutes_difference} hours after the start')
#         else:
#             print(f'{hours_difference}:{minutes_difference} hours after the start')





















































































































































































