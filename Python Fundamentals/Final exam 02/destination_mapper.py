# import re
# destinations = re.findall(r"=[A-Z][a-zA-z]{2,}=|/[A-Z][a-zA-Z]{2,}/", input())
# total = 0
# list = []
# for i in destinations:
#     if "=" in i:
#         i = i.replace('=', '')
#     elif "/" in i:
#         i = i.replace('/', '')
#     total += len(i)
#     list.append(i)
# print(f"Destinations: {', '.join(list)}")
# print(f"Travel Points: {total}")
#
#
#
import re
text = input()
destinations = re.findall(r"=[A-Z][A-Za-z]{2,}=|/[A-Z][A-Za-z]{2,}/", text)
total = 0
for i in range(len(destinations)):
    destinations[i] = destinations[i][1:-1]
    total += len(destinations[i])
print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {total}")
