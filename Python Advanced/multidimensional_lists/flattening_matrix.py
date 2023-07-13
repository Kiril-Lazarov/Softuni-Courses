n = int(input())
matrix = [[int(y) for y in (input().split(', '))] for x in range(n)]
flatt = [num for sublist in matrix for num in sublist]
print(flatt)