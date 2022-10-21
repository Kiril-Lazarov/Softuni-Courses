#
# data = input()
#
# while True:
#     stops = input()
#     if stops == 'Travel':
#         break
#     stops = stops.split(':')
#     if stops[0] == 'Add Stop':
#         index = int(stops[1])
#         destination = stops[2]
#         if index in range(len(data)):
#             data = data[:index] + destination + data[index:]
#     elif stops[0] == 'Remove Stop':
#         start = int(stops[1])
#         end = int(stops[2])
#         if start in range(len(data)) and end in range(len(data)):
#             data = data[:start] + data[end+1:]
#     elif stops[0] == 'Switch':
#         old = stops[1]
#         new = stops[2]
#         if old in data:
#             data = data.replace(old, new)
#     print(data)
# print(f"Ready for world tour! Planned stops: {data}")
#
#
stops = input()

while True:
    info = input()
    if info == "Travel":
        break
    actions = info.split(":")
    if actions[0] == 'Add Stop':
        index = int(actions[1])
        string = actions[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
    elif actions[0] == 'Remove Stop':
        start = int(actions[1])
        end = int(actions[2])
        if 0 <= start <= end < len(stops):
            stops = stops[:start] + stops[end+1:]
    elif actions[0] == 'Switch':
        old = actions[1]
        new = actions[2]
        stops = stops.replace(old, new)
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")
