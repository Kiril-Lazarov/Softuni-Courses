size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]

coordinates = input().split()
bomb_sequence = [[int(x) for x in pairs.split(',')] for pairs in coordinates]


def calculate_explosions(row, col):
    bomb_value =  matrix[row][col]
    if matrix[row][col] > 0:
        matrix[row][col] = 0
        for i in range(3):
            test_row = row + (i -1)
            if 0<= test_row < size:
                for j in range(3):
                    test_col = col +(j-1)
                    if 0<= test_col<size:
                        if matrix[test_row][test_col] >0:
                            matrix[test_row][test_col] -= bomb_value


for bomb_coordinates in bomb_sequence:
    row, col = bomb_coordinates

    calculate_explosions(row, col)
live_cells_counter = 0
sum_live_cells = 0
for row in matrix:
    live_cells = [x for x in row if x>0]
    live_cells_counter += len(live_cells)
    sum_live_cells += sum(live_cells)
print(f"Alive cells: {live_cells_counter}")
print(f"Sum: {sum_live_cells}")
for row in matrix:
    print(f'{" ".join([str(x) for x in row])}')




