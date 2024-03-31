def trace_calculate(row, col, sign):
    matrix[row][col] = sign

def inside(next_row, next_col):
    if 0 <= next_row < size and 0 <= next_col < size:
        return True
    trace_calculate(snake_row, snake_col, '.')
    return False


def move(snake_row, snake_col, direction):
    if direction == 'up':
        return snake_row - 1, snake_col
    elif direction == 'down':
        return snake_row + 1, snake_col
    elif direction == 'left':
        return snake_row, snake_col - 1
    elif direction == 'right':
        return snake_row, snake_col + 1


size = int(input())
matrix = []
snake_row = 0
snake_col = 0
first_borrow = ()
second_borrow = ()
food = 0

for rows in range(size):
    buffer = []
    row = input()
    for cols in row:
        buffer.append(cols)
    if 'S' in row:
        snake_row, snake_col = rows, row.index('S')
    if 'B' in row:
        if len(first_borrow) == 0:
            first_borrow = rows, row.index('B')
        elif len(second_borrow) == 0:
            second_borrow = rows, row.index('B')

    matrix.append(buffer)

while True:
    command = input()
    next_row, next_col = move(snake_row, snake_col, command)
    is_inside = inside(next_row, next_col)
    if not is_inside:
        break
    # matrix[snake_row][snake_col] = '.'

    if matrix[next_row][next_col] == '*':
        food += 1
        trace_calculate(snake_row, snake_col, '.')
        trace_calculate(next_row, next_col, 'S')
        snake_row, snake_col = next_row, next_col

    # matrix[snake_row][snake_col] = 'S'
    if food >=10:
        break
    if matrix[next_row][next_col] == 'B':
        if (next_row,next_col) == first_borrow:
            # matrix[next_row][next_col] = '.'
            trace_calculate(snake_row,snake_col, '.')
            trace_calculate(next_row, next_col, '.')
            snake_row, snake_col = second_borrow
            # matrix[snake_row][snake_col] = 'S'
            trace_calculate(snake_row, snake_col, 'S')
        else:
            trace_calculate(next_row, next_col, '.')
            snake_row, snake_col = first_borrow
            trace_calculate(snake_row, snake_col, 'S')
    if matrix[next_row][next_col] == '-':
        trace_calculate(snake_row, snake_col, '.')
        snake_row, snake_col = next_row, next_col
        trace_calculate(snake_row, snake_col, 'S')
if food >= 10:
    print("You won! You fed the snake.")
if not is_inside:
    print("Game over!")

print(f'Food eaten: {food}')
for row in matrix:
    print(''.join(row))