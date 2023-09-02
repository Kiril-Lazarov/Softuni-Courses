n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

p_matrix = []
s_matrix = []
for i in range(n):
    s_matrix.append(matrix[i][n - 1 - i])
    p_matrix.append(matrix[i][i])

print(f'Primary diagonal: {", ".join(map(str, p_matrix))}. Sum: {sum(p_matrix)}')
print(f'Secondary diagonal: {", ".join(map(str, s_matrix))}. Sum: {sum(s_matrix)}')
