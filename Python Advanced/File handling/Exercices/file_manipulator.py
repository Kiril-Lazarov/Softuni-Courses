import os

while True:
    data = input().split('-')
    if data[0] == 'End':
        break
    command = data[0]
    if command == 'Create':
        name, extension = data[1].split('.')
        with open(f'./{name}.{extension}', 'w') as file:
            pass
    elif command == 'Add':
        name, extension = data[1].split('.')
        content = data[2]
        with open(f'./{name}.{extension}', 'a') as file:
            file.write(f'{content}\n')
    elif command == 'Replace':
        file_name, old, new = data[1], data[2], data[3]
        if os.path.exists(file_name):
            with open(file_name,'r+') as file:
                content = file.read().replace(old, new)
            with open(file_name, 'w') as file:
                file.write(content)
    elif command == 'Delete':
        file_name = data[1]
        if os.path.exists(file_name):
            os.remove(file_name)


