n = int(input())
matrix = [[int(x) for x in input().split()] for y in range(n)]



def calculate(commmand, row,col, value):
    if commmand == 'Subtract':
        value *= -1
    matrix[row][col] += value

def validation(row, col):
    if 0 <= row<n and 0<= col<n:
        return True
    else:
        return False

while True:
    command = input().split()
    if command[0] == "END":
        for rows in matrix:
            print(*rows, sep=' ')
        break
    else:
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if validation(row,col):
            if command[0] == 'Add':
                calculate('Add', row, col, value)
            elif command[0] == "Subtract":
                calculate('Subtract', row, col, value)
        else:
            print('Invalid coordinates')