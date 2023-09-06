rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]
count = 0

for j in range(rows - 1):
    for i in range(cols - 1):
        if matrix[j][i] == matrix[j][i + 1] == matrix[j + 1][i] == matrix[j + 1][i + 1]:
            count += 1
print(count)
