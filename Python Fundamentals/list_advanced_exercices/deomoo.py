num_rows = int(input())
rows = []
rows1 = []
current = []
row_index_k = 0
col_index_k = 0
for i in range(num_rows):
    rows.append(input())
    for j in range(len(rows[i])):
        current.append(rows[i][j])
        if rows[i][j] == 'k':
            row_index_k = i
            col_index_k = j

    rows1.append(current)
    current = []

while True:
    if 0 < row_index_k < len(rows) and 0 < col_index_k < len(rows1[0]):
        if rows1[row_index_k - 1][col_index_k] == ' ':
            rows1[row_index_k - 1][col_index_k] = 'k'
            row_index_k -= 1
        elif rows1[row_index_k + 1][col_index_k] == ' ':
            rows1[row_index_k + 1][col_index_k] = 'k'
            row_index_k += 1
        elif rows1[row_index_k][col_index_k - 1] == ' ':
            rows1[row_index_k][col_index_k - 1] = 'k'
            col_index_k -= 1
        elif rows1[row_index_k][col_index_k + 1] == ' ':
            col_index_k += 1
            rows1[row_index_k][col_index_k + 1] = 'k'
    else:
        break
