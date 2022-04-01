# •	На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
# •	На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
# •	На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]
from math import floor
needed_hours = int(input())
days_available = int(input())
workers_count = int(input())

available_days_for_work = days_available * 0.9
total_hours = available_days_for_work * 8
additional_time_for_project = workers_count * days_available * 2
total_time = floor(total_hours + additional_time_for_project)

if total_time >= needed_hours:
    print(f'Yes!{abs(needed_hours - total_time)} hours left.')
else:
    print(f'Not enough time!{(needed_hours - total_time)} hours needed.')


    # print(available_days_for_work, total_hours, additional_time_for_project, total_time )