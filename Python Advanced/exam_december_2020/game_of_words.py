string = input()

n = int(input())
matrix = []
buffer = []
player_row = 0
player_col = 0

moves = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}
for i in range(n):
    row = input()
    for j in range(n):
        buffer.append(row[j])
        if row[j] == 'P':
            player_row, player_col = i, j
    matrix.append(buffer)
    buffer = []

m = int(input())

for _ in range(m):
    command = input()
    next_row, next_col = moves[command](player_row, player_col)
    if not 0<= next_row<n or not  0<= next_col <n:
        if string:
            string = string[:-1]
    else:
        if matrix[next_row][next_col].isalpha():
            string = string +  matrix[next_row][next_col]
            matrix[player_row][player_col] = '-'
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'
        else:
            matrix[player_row][player_col] = '-'
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'P'


print(string)
for row in matrix:
    print(''.join(row))
