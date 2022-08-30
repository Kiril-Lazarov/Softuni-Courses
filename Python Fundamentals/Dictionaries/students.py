data = input()
data_dictionary = {}
while ':' in data:
    data_list = data.split(':')
    name,id, course  = data_list[0], int(data_list[1]), data_list[2]
    if course not in data_dictionary:
        data_dictionary[course] = {}
    data_dictionary[course][id] = name
    data = input()

data = data.replace("_", ' ')

for id in data_dictionary[data]:
    print(f'{data_dictionary[data][id]} - {id}')
