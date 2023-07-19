n,m = (int(x) for x in input().split(', '))
matrix = []
m_sum = 0
for i in range(n):
    matrix.append([int(x) for x in input().split(', ')])
    m_sum += sum(matrix[i])
print(m_sum)
print(matrix)