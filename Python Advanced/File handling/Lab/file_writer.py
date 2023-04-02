import os
# file= open('./writer.txt', "w")
# file.write('This is my first file.\n')
# file.write('This is new bad line.\n')
# file.close()
# file = open('./text.txt', 'a')
# file.write('This is text.')
# file.write('This is a new text.\n')
# with open("./text.txt", "w") as f:
#     f.write("Hello World!!!")
file_path = './file.txt'
try:
    # if os.path.exists(file_path):

    os.remove('./file.txt')
except FileNotFoundError:
    print('Няма такъв')
