board = []
king_row, king_col = 0, 0
queens_positions_set = []
for i in range(8):
    row = input().split()
    if 'K' in row:
        king_row, king_col = i, row.index('K')
    board.append(row)

directions = ['lu','up','ru','l','r','ld','d','rd']


def move_pawn(row_step, col_step):
    next_row, next_col = king_row, king_col
    while True:
        next_row += row_step
        next_col += col_step
        if 0<=next_row<8  and 0<= next_col<8:
            if board[next_row][next_col] == 'Q':
                queens_positions_set.append([next_row, next_col])
                break
        else:
            break


def check_fields(direction):
    if direction == 'lu':
        move_pawn(-1,-1)
    elif direction == 'up':
        move_pawn(-1,0)
    elif direction == 'ru':
        move_pawn(-1, 1)
    elif direction == 'l':
        move_pawn(0, -1)
    elif direction == 'r':
        move_pawn(0, 1)
    elif direction == 'ld':
        move_pawn(1, -1)
    elif direction == 'd':
        move_pawn(1, 0)
    elif direction == 'rd':
        move_pawn(1,1 )



for direction in directions:
    check_fields(direction)
if queens_positions_set:
    print(*queens_positions_set, sep= '\n')
else:
    print('The king is safe!')
