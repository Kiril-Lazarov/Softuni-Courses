# num_rows = int(input())
# rows = []
# rows1 = []
# current = []
# row_index_k = 0
# col_index_k = 0
# for i in range(num_rows):
#     rows.append(input())
#     for j in range(len(rows[i])):
#         current.append(rows[i][j])
#         if rows[i][j] == 'k':
#             row_index_k = i
#             col_index_k = j
#
#     rows1.append(current)
#     current = []
#
# while True:
#     if 0 < row_index_k < len(rows):
#         if 0 < col_index_k < len(rows1[0]):
#             if rows1[row_index_k - 1][col_index_k] == ' ':
#                 rows1[row_index_k - 1][col_index_k] = 'k'
#                 row_index_k -= 1
#             elif rows1[row_index_k + 1][col_index_k] == ' ':
#                 rows1[row_index_k + 1][col_index_k] = 'k'
#                 row_index_k += 1
#             elif rows1[row_index_k][col_index_k - 1] == ' ':
#                 rows1[row_index_k][col_index_k - 1] = 'k'
#                 col_index_k -= 1
#             elif rows1[row_index_k][col_index_k + 1] == ' ':
#                 col_index_k += 1
#                 rows1[row_index_k][col_index_k + 1] = 'k'

n = int(input())
maze = []
kate_row, kate_col = 0, 0
for rows in range(n):
    line = list(input())
    maze.append(line)
    if 'k' in line:
        kate_row, kate_col = rows, line.index('k')
directions = ['up', 'down', 'left', 'right']
max_count = 0
steps = {
    'up': lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
rows_length = len(maze[0])

steps_count = 0
find_path = False



def first_look_around(row, col, steps_count):
    for direction in directions:
        global max_count
        global  find_path
        next_row, next_col = steps[direction](row, col)
        if 0 <= next_row < n and 0 <= next_col < rows_length:
            if maze[next_row][next_col] == ' ':
                maze[next_row][next_col] = 'k'

                if next_row == 0 or next_row == n-1 or next_col == 0 or next_col == rows_length -1:
                    if steps_count > max_count-1:
                        max_count = steps_count +1
                    find_path = True
                else:
                    steps_count += 1

                first_look_around(next_row, next_col, steps_count)


first_look_around(kate_row, kate_col, steps_count)


if find_path:
    print(f"Kate got out in {max_count + 1} moves")
else:
    print("Kate cannot get out")
