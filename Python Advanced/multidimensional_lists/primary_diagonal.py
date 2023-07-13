n = int(input())

matrix = [[int(x) for x in input().split(' ')] for x in range(n)]

print(sum([matrix[i][i] for i in range(n)]))