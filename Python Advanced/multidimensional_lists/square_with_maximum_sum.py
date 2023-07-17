n,m = (int(x) for x in input().split(', '))
matrix = [[int(x) for x in input().split(', ')] for i in range(n)]

total_sum = 0
biggest_matrix_sum = 0
win_matrix = []
for i in range(n-1):
    for k in range(m-1):
        submatrix = [matrix[i][k], matrix[i][k+1], matrix[i+1][k], matrix[i+1][k+1]]
        total_sum += sum(submatrix)
        if total_sum > biggest_matrix_sum:
            biggest_matrix_sum = total_sum
            win_matrix = submatrix
        total_sum = 0

print(f'{" ".join(map(str,win_matrix[:2]))}\n{" ".join(map(str, win_matrix[2:]))}')
print(biggest_matrix_sum)
