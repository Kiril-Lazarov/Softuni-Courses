def get_next_position(alice_rows, alice_cols, direction):
    if direction == 'up':
        return alice_rows - 1, alice_cols
    elif direction == 'down':
        return alice_rows + 1, alice_cols
    elif direction == 'left':
        return alice_rows, alice_cols - 1
    elif direction == 'right':
        return alice_rows, alice_cols + 1


n = int(input())
alice_rows = 0
alice_cols = 0
matrix = []
tea_bags = 0

# steps = {
#     'left': lambda r, c: (r, c - 1),
#     'right': lambda r, c: (r, c + 1),
#     'up': lambda r, c: (r - 1, c),
#     'down': lambda r, c: (r + 1, c),
# }
for i in range(n):
    row = input().split()
    if 'A' in row:
        alice_rows = i
        alice_cols = row.index('A')
    matrix.append([x for x in row])

while tea_bags < 10:
    matrix[alice_rows][alice_cols] = "*"
    direction = input()
    next_row, next_col  = get_next_position(alice_rows, alice_cols, direction)
    if next_row <0 or next_col < 0 or next_row>= n or next_col >= n:
        break
    alice_rows, alice_cols = next_row, next_col



    if matrix[alice_rows][alice_cols] == '.' or matrix[alice_rows][alice_cols]== '*':
        continue
    if matrix[alice_rows][alice_cols] == 'R':

        break
    tea_bags += int(matrix[alice_rows][alice_cols])
matrix[alice_rows][alice_cols] = "*"
if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))
