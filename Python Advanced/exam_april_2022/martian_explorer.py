matrix = []
rover_row, rover_col = 0, 0
for i in range(6):
    row = input().split()
    for j in row:
        if j == 'E':
            rover_row, rover_col = i, row.index(j)


    matrix.append(row)

commands = input().split(', ')
is_found_supplies = []

def next_move(row,col, command):
    if command == 'left':
        return row, col - 1
    elif command == 'right':
        return row, col + 1
    elif command == 'up':
        return row - 1, col
    elif command == 'down':
        return row +1, col

for command in commands:
    next_row, next_col = next_move(rover_row, rover_col, command)
    if next_row < 0:
        next_row = 5
    if next_row > 5:
        next_row = 0
    if next_col < 0:
        next_col = 5
    if next_col > 5:
        next_col = 0
    if matrix[next_row][next_col] == 'R':
        print(f"Rover got broken at ({next_row}, {next_col})")
    if matrix[next_row][next_col] == 'W':
        print(f"Water deposit found at ({next_row}, {next_col})")
        if "water" not in is_found_supplies:
            is_found_supplies.append('Water')
    elif matrix[next_row][next_col] == 'M':
        print(f"Metal deposit found at ({next_row}, {next_col})")
        if "Metal" not in is_found_supplies:
            is_found_supplies.append('Metal')
    elif matrix[next_row][next_col] == 'C':
        print(f"Concrete deposit found at ({next_row}, {next_col})")
        if "Concrete" not in is_found_supplies:
            is_found_supplies.append('Concrete')
    matrix[rover_row][rover_col] = '-'
    rover_row, rover_col = next_row, next_col
    matrix[rover_row][rover_col] = 'E'
if len(is_found_supplies) >= 3:
    print( "Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
