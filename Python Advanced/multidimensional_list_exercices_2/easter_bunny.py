# n = int(input())
# field = [[j for j in input().split()] for i in range(n)]
#
# direction_list = ['left', 'right', 'up', 'down']
# eggs = [0]
#
# best_dir = ['']
# path = []
# best_path = []
# max_eggs = [float('inf')]
#
#
# def compare(eggs, path, max_eggs, direction, best_path):
#     if eggs[0] > max_eggs[0]:
#         best_path = []
#         max_eggs[0] = eggs[0]
#         best_dir[0] = direction
#         for i in path:
#             best_path.append(i)
#         if direction == 'down':
#             print(best_dir[0])
#
#             for i in best_path:
#                 print(i)
#             print(max_eggs[0])
#
#
# def go_func(direction, rows, cols, best_path):
#
#
#     for dir in direction:
#         path = []
#         eggs = [0]
#         if dir == 'left':
#
#             if cols != 0:
#                 for i in range(cols, -1, -1):
#                     if field[rows][i].isdigit():
#                         eggs[0] += int(field[rows][i])
#                         path.append([rows, i])
#                     elif field[rows][i] == 'X':
#                         break
#                 if eggs[0] >= 1:
#                     compare(eggs, path, max_eggs, dir, best_path)
#
#         elif dir == "right":
#
#             if cols != n:
#                 for i in range(cols, n):
#                     if field[rows][i].isdigit():
#                         eggs[0] += int(field[rows][i])
#                         path.append([rows, i])
#                     elif field[rows][i] == 'X':
#                         break
#                 if eggs[0] >= 1:
#                     compare(eggs, path, max_eggs, dir, best_path)
#
#         elif dir == "up":
#             if rows != 0:
#
#                 for i in range(rows, -1, -1):
#                     if field[i][cols].isdigit():
#                         eggs[0] += int(field[i][cols])
#                         path.append([i, cols])
#                     elif field[i][cols] == 'X':
#                         break
#                 if eggs[0] >= 1:
#                     compare(eggs, path, max_eggs, dir, best_path)
#
#         elif dir == "down":
#
#             if rows != n:
#                 for i in range(rows, n):
#                     if field[i][cols].isdigit():
#                         eggs[0] += int(field[i][cols])
#                         path.append([i, cols])
#
#                     elif field[i][cols] == 'X':
#                         break
#                 if eggs[0] >= 1:
#                     compare(eggs, path, max_eggs, dir, best_path)
#
#
# is_finish = False
# for i in range(n):
#     for j in range(n):
#         if field[i][j] == "B":
#             rows = i
#             cols = j
#             go_func(direction_list, rows, cols, best_path)
#             is_finish = True
#             break
#         if is_finish:
#             break
#     if is_finish:
#         break

n = int(input())
field = []
best_sum = float('-inf')
best_dir = ''
best_path = []

bunny_rows = 0
bunny_cols = 0
for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == 'B':
            bunny_rows = row
            bunny_cols = col

    field.append(row_elements)
directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_rows, bunny_cols)
    current_path = []
    while 0 <= row < n and 0 <= col < n and field[row][col] != "X":
        current_sum += int(field[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)
    if current_sum > best_sum and current_path:
        best_sum = current_sum
        best_dir = direction
        best_path = current_path

print(best_dir)
print(*best_path, sep='\n')
print(best_sum)
