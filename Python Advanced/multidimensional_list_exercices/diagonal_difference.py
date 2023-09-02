n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

p_matrix = []
s_matrix = []
for i in range(n):
    s_matrix.append(matrix[i][n - 1 - i])
    p_matrix.append(matrix[i][i])
print(f'{abs(sum(p_matrix)- sum(s_matrix))}')

