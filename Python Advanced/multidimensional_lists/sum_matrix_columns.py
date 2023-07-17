n, m = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(' ')] for i in range(n)]

the_sum = 0
for columns in range(m):
    for rows in range(n):
        the_sum += matrix[rows][columns]
    print(the_sum)
    the_sum = 0

