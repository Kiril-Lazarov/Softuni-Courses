n, m = [int(x) for x in input().split()]
matrix = []
buffer = []
string = input()*2*n
for i in range(n):
    for j in range(m):
        buffer.append(string[j])
    if i % 2 == 0:
        matrix.append(buffer)
    else:
        matrix.append((buffer[::-1]))
    string = string[m:]
    buffer = []
a = [print(*matrix[i], sep='') for i in range(n)]
