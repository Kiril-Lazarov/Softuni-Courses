rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]


def check_index(command):
    first = (int(command[1]), int(command[2]))
    second = (int(command[3]), int(command[4]))
    if 0 <= first[0] < rows and 0 <= first[1] < cols and 0 <= second[0] < rows and 0 <= second[1] < cols:
        return True
    else:
        return False


while True:
    command = input().split()
    if command[0] == "END":
        break
    if len(command) != 5 or command[0] != 'swap' or not check_index(command):
        print('Invalid input!')
    else:
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = matrix[int(command[3])] \
        [int(command[4])], matrix[int(command[1])][int(command[2])]
        for i in range(rows):
            print(*matrix[i], sep=' ')

