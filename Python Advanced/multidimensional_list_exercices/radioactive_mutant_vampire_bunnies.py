n, m = [int(x) for x in input().split(' ')]
player_row, player_col = 0, 0
matrix = []
buffer = []
for i in range(n):
    row = input()
    for j in range(m):
        buffer.append(row[j])
        if row[j] == 'P':
            player_row = i
            player_col = j

    matrix.append(buffer)
    buffer = []


def moves(row, col, direction):
    if direction == 'U':
        return row - 1, col
    elif direction == 'D':
        return row + 1, col
    elif direction == 'L':
        return row, col - 1
    elif direction == 'R':
        return row, col + 1


commands = input()


def bunnies_multiplication(row, col):
    if 0 <= row - 1:
        if matrix[row - 1][col] == '.':
            matrix[row - 1][col] = 'b'
        elif matrix[row - 1][col] == 'P':
            return True
    if row + 1 < n:
        if matrix[row + 1][col] == '.':
            matrix[row + 1][col] = 'b'
        elif matrix[row + 1][col] == 'P':
            return True
    if 0 <= col-1:
        if matrix[row][col - 1] == '.':
            matrix[row][col - 1] = 'b'
        elif matrix[row][col - 1] == 'P':
            return True
    if col + 1 < m:
        if matrix[row][col + 1] == '.':
            matrix[row][col + 1] = 'b'
        elif matrix[row][col + 1] == 'P':
            return True

    return False


def recalibrate_matrix():
    for rows in range(n):
        for cols in range(m):
            if matrix[rows][cols] == 'b':
                matrix[rows][cols] = 'B'



def check_for_bunnies():
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 'B':
                is_hitted = bunnies_multiplication(row, col)
                if is_hitted:
                    return False
    recalibrate_matrix()

    return True


is_player_alive = True
for letter in commands:
    next_row, next_col = moves(player_row, player_col, letter)
    matrix[player_row][player_col] = '.'

    is_player_alive = check_for_bunnies()
    if 0<= next_row< n and 0<= next_col<m:
        if matrix[next_row][next_col] == 'B':
            player_row, player_col = next_row, next_col
            is_player_alive = False
            break
    else:
        break
    player_row, player_col = next_row, next_col
    matrix[player_row][player_col] = 'P'

for rows in matrix:
    print(f'{"".join(rows)}')
if is_player_alive:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")


