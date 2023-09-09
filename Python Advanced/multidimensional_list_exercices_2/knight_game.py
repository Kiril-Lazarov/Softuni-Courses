# n = int(input())
# board = [[j for j in input()] for i in range(n)]
# hits = [0]
#
#
# def check_cell(tested_cell):
#     if board[tested_cell[0]][tested_cell[1]] == "K":
#         hits[0] += 1
#         board[tested_cell[0]][tested_cell[1]] = "0"
#
#
# def check_values(rows, cols):
#     tested_cell = []
#     location = [rows, cols]
#
#     if location[0] - 2 >= 0:
#         if location[1] - 1 >= 0:
#             tested_cell = [location[0] - 2, location[1] - 1]
#             check_cell(tested_cell)
#         if location[1] + 1 < n:
#             tested_cell = [location[0] - 2, location[1] + 1]
#             check_cell(tested_cell)
#     if location[0] + 2 < n:
#
#         if location[1] >= 1:
#             tested_cell = [location[0] + 2, location[1] - 1]
#             check_cell(tested_cell)
#         if location[1] + 1 < n:
#             tested_cell = [location[0] + 2, location[1] + 1]
#             check_cell(tested_cell)
#     if location[1] - 2 >= 0:
#         if location[0] - 1 >= 0:
#             tested_cell = [location[0] - 1, location[1] - 2]
#             check_cell(tested_cell)
#         if location[0] + 1 < n:
#             tested_cell = [location[0] + 1, location[1] - 2]
#             check_cell(tested_cell)
#     if location[1] + 2 < n:
#         if location[0] - 1 >= 0:
#             tested_cell = [location[0] - 1, location[1] + 2]
#             check_cell(tested_cell)
#         if location[0] + 1 < n:
#             tested_cell = [location[0] + 1, location[1] + 2]
#             check_cell(tested_cell)
#
#
# for x in range(n):
#     for y in range(n):
#         if board[x][y] == 'K':
#             check_values(x, y)
#
#     # print(''.join(board[x]))
# print(hits[0])
max_hits = 0
n = int(input())
removed_knights = 0
buffer = []
matrix = []
for i in range(n):
    row = input()
    for j in range(n):
        buffer.append(row[j])
    matrix.append(buffer)
    buffer = []

moves = {
    'up': lambda r, c, step: (r - step, c),
    'down': lambda r, c, step: (r + step, c),
    'left': lambda r, c, step: (r, c - step),
    'right': lambda r, c, step: (r, c + step)
}


def knight_moves(row, col):
    k_hits = 0
    sequence = ['up', 'down', 'left', 'right']
    for direction in sequence:
        if direction == 'up' or direction == 'down':
            for j in range(2):
                if j == 0:
                    const = -1
                else:
                    const = 1
                test_row, test_col = moves[direction](row, col + const, 2)
                if 0 <= test_row < n and 0 <= test_col < n:
                    if matrix[test_row][test_col] == 'K':
                        k_hits += 1

        else:
            for j in range(2):
                if j == 0:
                    const = -1
                else:
                    const = 1
                test_row, test_col = moves[direction](row + const, col, 2)
                if 0 <= test_row < n and 0 <= test_col < n:
                    if matrix[test_row][test_col] == 'K':
                        k_hits += 1
    return k_hits

while True:
    best_row, best_col = 0, 0
    number_of_hits = 0
    max_hits = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'K':
                knight_row, knight_col = i, j
                number_of_hits = knight_moves(knight_row, knight_col)
                if number_of_hits > max_hits:
                    max_hits = number_of_hits
                    best_row, best_col = knight_row, knight_col
    if max_hits != 0:
        matrix[best_row][best_col] = '0'


        removed_knights +=1
    else:
        break
print(removed_knights)
