# import re
# text = re.findall(r"\|([a-zA-Z ]+)\|([\d]{2}\/[\d]{2}\/[\d]{2})\|([\d]+)\||#([a-zA-Z ]+)#([\d]{2}\/[\d]{2}\/[\d]{2})#([\d]+)#", input())
# items_list = []
# total = 0
# new = ()
# for i in text:
#     if i[0] == '':
#         i = i[3:]
#
#
#     else:
#         i = i[:3]
#     total += int(i[2])
#     items_list.append(i)
# total =total  // 2000
# print(f"You have food to last you for: {total} days!")
# for i in items_list:
#     print(f"Item: {i[0]}, Best before: {i[1]}, Nutrition: {i[2]}")
#

import re
text = input()
data = re.findall(r"#[A-Z a-z]+#[0-9]{2}/[0-9]{2}/[0-9]{2}#[\d]+#|\|[A-Z a-z]+\|[0-9]{2}/[0-9]{2}/[0-9]{2}\|[\d]+\|", text)
total_nutrition = 0
for items in range(len(data)):
    if "#" in data[items]:
        data[items] = data[items].split("#")
    elif "|" in data[items]:
        data[items] = data[items].split('|')
    while "" in data[items]:
        data[items].remove('')
    total_nutrition += int(data[items][2])
print(f"You have food to last you for: {total_nutrition//2000} days!")
for items in data:
    print(f"Item: {items[0]}, Best before: {items[1]}, Nutrition: {items[2]}")

