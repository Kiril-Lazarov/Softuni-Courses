def add_numbers(row, col):
    for i in range(-1, 2):
        if 0 <= row + i < size:
            for j in range(-1, 2):
                if 0 <= col + j < size:
                    if matrix[row + i][col + j] != '*':
                        matrix[row + i][col + j] += 1


size = int(input())
number_boms = int(input())
matrix = []
buffer = []
addresses = []
for i in range(size):
    for j in range(size):
        buffer.append(0)
    matrix.append(buffer)
    buffer = []

for _ in range(number_boms):
    bomb_row, bomb_col = (int(x) for x in input().strip('()').split(', '))
    matrix[bomb_row][bomb_col] = '*'
    addresses.append((bomb_row, bomb_col))

for address in addresses:
    row, col = address
    add_numbers(row, col)

for row in matrix:
    print(' '.join(str(x) for x in row))
