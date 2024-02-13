chessboard = []
w_row, w_col = 0, 0
b_row, b_col = 0, 0
turns = ['w', 'b']
is_winner = False
col_coordinates_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
row_coordinates_nums = [8,7,6,5,4,3,2,1]
for i in range(8):
    row = input().split()
    for j in row:
        if j == 'b':
            b_row = i
            b_col = row.index(j)
        if j == 'w':
            w_row = i
            w_col = row.index(j)
    chessboard.append(row)


def find_enemy(row, col, letter):
    if letter == 'w':
        if 0<= col -1<8:
            if chessboard[row -1][col -1]== 'b':
                return True
        if 0<= col +1<8:
            if chessboard[row -1][col +1] == 'b':
                return True
    elif letter == 'b':
        if 0<= col+1< 8:
            if chessboard[row +1][col+1]== 'w':
                return True
        if 0<= col-1< 8:
            if chessboard[row +1][col-1]== 'w':
                return True
    return False


def find_name(row, col):
    return f'{col_coordinates_letters[col]}{row_coordinates_nums[row]}'


while True:
    for letter in turns:
        if letter == 'w':
            chessboard[w_row][w_col] = '-'
            if find_enemy(w_row,w_col, letter):
                square = find_name(b_row,b_col)
                print(f"Game over! White win, capture on {square}.")
                is_winner = True
                break
            if w_row != 0:
                w_row -= 1
            if w_row == 0:
                square = find_name(w_row, w_col)
                print(f"Game over! White pawn is promoted to a queen at {square}.")
                is_winner = True
                break
            chessboard[w_row][w_col] = 'w'
        if letter == 'b':
            chessboard[b_row][b_col] = '-'
            if find_enemy(b_row, b_col, letter):
                square = find_name(w_row, w_col)
                print(f"Game over! Black win, capture on {square}.")
                is_winner = True
                break
            if b_row != 7:
                b_row += 1
            chessboard[b_row][b_col] = 'b'
            if b_row == 7:
                square = find_name(b_row, b_col)
                print(f"Game over! Black pawn is promoted to a queen at {square}.")
                is_winner = True
                break
    if is_winner:
        break


