n = int(input())

matrix = [input() for x in range(n)]

symbol = input()



def find_symbol(matrix, n):
    for rows_index in range(n):
        for col_index in range(n):
            if matrix[rows_index][col_index] == symbol:
                return (rows_index, col_index)


a = find_symbol(matrix, n)
if a != None:
    print(a)
else:
    print(f'{symbol} does not occur in the matrix')
