n = int(input())
matrix = []
player_path = []
player_row, player_col = 0, 0
total_coins = 0
for i in range(n):
    row = [int(x) if x.isdigit() else str(x) for x in input().split()]
    if 'P' in row:
        player_row, player_col = i, row.index("P")
        player_path.append([player_row, player_col])
    matrix.append(row)


def moves(player_row, player_col, command):
    if command == 'left':
        return player_row, player_col - 1
    elif command == 'right':
        return player_row, player_col + 1

    elif command == 'up':
        return player_row - 1, player_col
    elif command == 'down':
        return player_row + 1, player_col


while True:
    command = input()
    if command not in 'left, right, up, down':
        continue

    matrix[player_row][player_col] = 0
    next_row, next_col = moves(player_row, player_col, command)
    if next_row < 0:
        next_row = n - 1
    if next_row == n:
        next_row = 0
    if next_col < 0:
        next_col = n - 1
    if next_col == n:
        next_col = 0
    if matrix[next_row][next_col] == 'X':
        player_path.append([next_row, next_col])
        break
    player_row, player_col = next_row, next_col
    player_path.append([player_row, player_col])
    if matrix[player_row][player_col] != 0:
        total_coins += matrix[player_row][player_col]

        if total_coins >= 100:
            break

if total_coins>= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    total_coins = int(total_coins/2)
    print(f"Game over! You've collected {total_coins} coins.")
print('Your path:')
for path in player_path:
    print(path)
