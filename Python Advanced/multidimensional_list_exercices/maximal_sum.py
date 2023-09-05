rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for x in range(rows)]
big_sum = float('-inf')
big_matrix = []


def matrix_summation(sub_matrix):
    the_sum = sum([sum(x) for x in sub_matrix])
    return the_sum


for i in range(rows - 2):
    for j in range(cols - 2):
        sub_matrix = [
            [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
            [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
            [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
        ]
        total_sum = matrix_summation(sub_matrix)

        if total_sum > big_sum:
            big_sum = total_sum
            big_matrix = sub_matrix

print(f'Sum = {big_sum}')
for i in range(3):
    print(" ".join(map(str, big_matrix[i])))
