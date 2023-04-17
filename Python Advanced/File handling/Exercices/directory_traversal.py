import os
from os.path import isdir, join

file_extensions = {}


def append_file(file):
    file_info = file.split('.')
    name, ext = file_info[0], file_info[-1]
    if ext not in file_extensions:
        file_extensions[ext] = []
    file_extensions[ext].append(name)


def check_directory(file_path):
    for file in os.listdir(file_path):
        next_file_path = (join(os.path.abspath(file_path), file))
        if isdir(next_file_path):
            check_directory(next_file_path)
        else:
            append_file(file)


names = os.listdir('./')

for files in names:
    if isdir(files):
        file_path = os.path.abspath(files)
        check_directory(file_path)
    else:
        append_file(files)

file_extensions = {k: v for k, v in sorted(file_extensions.items(), key=lambda x: (x[0], x[1]))}

with open('./report.txt', 'w') as file:
    for key, value in file_extensions.items():
        file.write(f'.{key}\n')
        for values in value:
            file.write((f'- - - {values}.{key}\n'))


