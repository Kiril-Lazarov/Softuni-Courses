from collections import deque

working_robots = {}
available_robots = {}
items_seq = deque()


def time_transform(string):
    return int(string[0]) * 3600 + int(string[1]) * 60 + int(string[2])


def conversion(seconds):
    hours = seconds // 3600
    hours_remainder = seconds % 3600
    if hours >= 24:
        hours %= 24
    minutes = hours_remainder // 60
    minutes_remainder = hours_remainder % 60

    if hours < 10:
        hours = f'{0}{hours}'
    if minutes < 10:
        minutes = f'{0}{minutes}'
    if minutes_remainder < 10:
        minutes_remainder = f'{0}{minutes_remainder}'
    return f'{hours}:{minutes}:{minutes_remainder}'

info = (input().split(';'))
start_time = time_transform(input().split(":"))

while True:
    item = input()
    if item == "End":
        break
    items_seq.append(item)
seconds = 0


working_time = 0
for i in range(len(info)):

    name = info[i].split("-")[0]
    working_time =  int(info[i].split("-")[1])
    working_robots[name] = {'Processing time':working_time}
    available_robots[name] = 0


def decrease_time():
    for name, time in available_robots.items():
        if time !=0:
            available_robots[name] -= 1

    return available_robots


def give_item_to_robot():
    for name, time in available_robots.items():
        if time == 0:
            available_robots[name] = working_robots[name]['Processing time']
            print(f'{name} - {curr_item} [{conversion(start_time + seconds)}]')
            return True
    return False

while items_seq:
    seconds+=1
    is_get_item = False
    curr_item = items_seq.popleft()
    available_robots = decrease_time()
    if not give_item_to_robot():
        items_seq.append(curr_item)





