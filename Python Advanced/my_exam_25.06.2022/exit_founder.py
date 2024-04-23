import re

first_player, second_player = input().split(', ')
matrix = []
first_rest = False
second_rest = False
for rows in range(6):
    line = input().split(' ')
    matrix.append(line)
turn = 0
while True:
    turn += 1
    if turn % 2 == 1:
        player = first_player

    else:
        player = second_player


    command = input().strip()
    numbers = re.findall(r'\d+', command)
    row, col = int(numbers[0]), int(numbers[-1])
    if player == first_player and not first_rest:
        if matrix[row][col] == 'W':
            print(f"{player} hits a wall and needs to rest.")
            first_rest = True
        elif matrix[row][col] == 'E':
            print(f"{player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            winner = second_player
            print(f"{player} is out of the game! The winner is {winner}.")
            break
    elif player == first_player and first_rest:
        first_rest = False


    if player ==second_player and not second_rest:
        if matrix[row][col] == 'W':
            print(f"{player} hits a wall and needs to rest.")
            second_rest = True
        elif matrix[row][col] == 'E':
            print(f"{player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == 'T':
            winner = first_player
            print(f"{player} is out of the game! The winner is {winner}.")
            break
    elif player ==second_player and  second_rest:
        second_rest = False
