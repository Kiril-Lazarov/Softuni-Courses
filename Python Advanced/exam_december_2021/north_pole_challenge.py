rows, columns = [int(x) for x in input().split(', ')]
items = ['G', 'D', 'C']
colected_signs = []
matrix = []
total_items = 0
my_row, my_col = 0, 0
is_done = False
for row in range(rows):
    signs = input().split()
    buffer = []
    for col in signs:
        if col in items:
            total_items += 1
        if col == 'Y':
            my_row = row
            my_col = signs.index(col)
        buffer.append(col)
    matrix.append(buffer)





while True:
    command = input()
    if command == 'End':
        break
    direction, step = command.split('-')
    next_row, next_col = my_row, my_col
    if direction == 'left':
        for _ in range(int(step)):
            next_col -= 1
            if next_col < 0:
                next_col = columns -1
            if matrix[next_row][next_col]  in items:
                colected_signs.append(matrix[next_row][next_col])
            matrix[my_row][my_col] = 'x'
            matrix[next_row][next_col] = 'Y'
            my_col = next_col
            if len(colected_signs) == total_items:
                print('Merry Christmas!')
                is_done = True
                break


    elif direction == 'right':
        for _ in range(int(step)):
            next_col += 1
            if next_col >columns-1:
                next_col = 0
            if matrix[next_row][next_col]  in items:
                colected_signs.append(matrix[next_row][next_col])
            matrix[my_row][my_col] = 'x'
            matrix[next_row][next_col] = 'Y'
            my_col = next_col
            if len(colected_signs) == total_items:
                print('Merry Christmas!')
                is_done = True
                break


    elif direction == 'up':
        for _ in range(int(step)):
            next_row -= 1
            if next_row <0:
                next_row = rows -1
            if matrix[next_row][next_col]  in items:
                colected_signs.append(matrix[next_row][next_col])
            matrix[my_row][my_col] = 'x'
            matrix[next_row][next_col] = 'Y'
            my_row = next_row
            if len(colected_signs) == total_items:
                print('Merry Christmas!')
                is_done = True
                break
    elif direction == 'down':
        for _ in range(int(step)):
            next_row += 1
            if next_row > rows-1:
                next_row = 0
            if matrix[next_row][next_col] in items:
                colected_signs.append(matrix[next_row][next_col])
            matrix[my_row][my_col] = 'x'
            matrix[next_row][next_col] = 'Y'
            my_row = next_row
            if len(colected_signs) == total_items:
                print('Merry Christmas!')
                is_done = True
                break
    if is_done:
        break
decorations = colected_signs.count('D')
gifts = colected_signs.count('G')
cookies = colected_signs.count('C')
print("You've collected:")
print(f'- {decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f"- {cookies} Cookies")

for row in matrix:
    print(' '.join(row))

