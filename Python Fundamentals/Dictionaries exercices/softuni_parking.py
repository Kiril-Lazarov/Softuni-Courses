def register(data, parking_data_dict):
    if data[1] not in parking_data_dict:
        parking_data_dict[data[1]] = data[2]
        print(f"{data[1]} registered {data[2]} successfully")
    else:
        print(f"ERROR: already registered with plate number {data[2]}")


def unregister(data, parking_data_dict):
    if data[1] not in parking_data_dict:
        print(f"ERROR: user {data[1]} not found")
    else:
        del parking_data_dict[data[1]]
        print(f"{data[1]} unregistered successfully")


def final_print(parking_data_dict):
    final = {print(f"{key} => {value}") for (key, value) in parking_data_dict.items()}


def softuni_parking():
    parking_data_dict = {}
    n = int(input())
    for i in range(n):
        data = input().split(' ')
        if data[0] == 'register':
            register(data, parking_data_dict)
        elif data[0] == 'unregister':
            unregister(data, parking_data_dict)
    final_print(parking_data_dict)


softuni_parking()
