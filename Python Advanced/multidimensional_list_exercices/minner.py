n = int(input())
directions_sequence = [x for x in input().split(' ')]
matrix = []
total_coals = 0
miner_row = 0
miner_col = 0
game_over = False
if n != 0:
    for i in range(n):
        row = [x for x in input().split(' ')]
        total_coals += row.count('c')
        for j in range(n):
            if row[j] == 's':
                miner_row, miner_col = i, j
        matrix.append(row)


def moves(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


for direction in directions_sequence:
    next_row, next_col = moves(miner_row, miner_col, direction)
    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == 'e':
            print(f"Game over! ({next_row}, {next_col})")
            game_over = True
            break
        elif matrix[next_row][next_col] == 'c':
            total_coals -= 1
            if total_coals == 0:
                miner_row, miner_col = next_row, next_col
                break
        matrix[miner_row][miner_col] = '*'
        matrix[next_row][next_col] = 's'
        miner_row, miner_col = next_row, next_col
if total_coals == 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")

elif not game_over and total_coals != 0:
    print(f"{total_coals} pieces of coal left. ({miner_row}, {miner_col})")
