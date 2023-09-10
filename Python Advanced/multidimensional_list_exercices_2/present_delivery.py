presents = int(input())
syze = int(input())
good_kids = 0
gifted_good_kids = 0
matrix = []
santa_row = 0
santa_col = 0
presents_given = 0
moves = {
    'left': lambda r, c, s: (r, c - s),
    'right': lambda r, c, s: (r, c + s),
    'up': lambda r, c, s: (r - s, c),
    'down': lambda r, c, s: (r + s, c),
}
for i in range(syze):
    rows = input().split()
    good_kids += rows.count('V')
    if 'S' in rows:
        santa_row, santa_col = i, rows.index('S')
    matrix.append(rows)


def give_presents(next_row, next_col):
    global presents_given
    global gifted_good_kids
    gifted_kids = 0
    for direction, counters in moves.items():
        checked_row, checked_col = counters(next_row, next_col, 1)
        if matrix[checked_row][checked_col] != 'S':
            if matrix[checked_row][checked_col] != '-':
                if matrix[checked_row][checked_col] == 'V':
                    gifted_good_kids += 1
                if matrix[checked_row][checked_col] != 'C':
                    matrix[checked_row][checked_col] = '-'
                presents_given += 1
                if presents - presents_given == 0:
                    break
                if good_kids - gifted_good_kids == 0:
                    break

    return presents_given, gifted_good_kids


while True:
    command = input()
    if command == 'Christmas morning':
        break
    next_row, next_col = moves[command](santa_row, santa_col, 1)
    if 0 <= next_row < syze and 0 <= next_col < syze:
        if matrix[next_row][next_col] == 'V':
            gifted_good_kids += 1
            presents_given += 1
        elif matrix[next_row][next_col] == 'C':
            presents_given, gifted_good_kids = give_presents(next_row, next_col)
        matrix[santa_row][santa_col] = '-'
        santa_row, santa_col = next_row, next_col
        matrix[santa_row][santa_col] = 'S'
        if good_kids - gifted_good_kids == 0:
            break
        if presents == presents_given:
            break

if presents == presents_given and good_kids - gifted_good_kids>0:
    print('Santa ran out of presents!')
for rows in matrix:
    print(' '.join(rows))
if good_kids != gifted_good_kids:
    print(f'No presents for {good_kids - gifted_good_kids} nice kid/s.')

else:

    print(f'Good job, Santa! {good_kids} happy nice kid/s.')

