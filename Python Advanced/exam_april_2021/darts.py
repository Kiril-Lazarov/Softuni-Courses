import re
player_one, player_two = input().split(', ')

matrix = [input().split() for x in range(7)]
turns = 1
is_winner = False
winner = ''
row = 0
col = 0
sequence = (player_one, player_two)
players = {
    player_one: 501,
    player_two: 501
}


def find_digits(row, col):
    digits = []
    digits.append(int(matrix[row][0]))
    digits.append(int(matrix[row][6]))
    digits.append(int(matrix[0][col]))
    digits.append(int(matrix[6][col]))
    return digits


while True:

    for name in sequence:
        data = str(input())
        numbers = re.findall(r'\d+', data)
        row, col = int(numbers[0]), int(numbers[1])
        if row < 7 and col < 7:
            if matrix[row][col].isdigit():
                players[name] -= int(matrix[row][col])
                if players[name] <= 0:
                    is_winner = True
                    winner = name
                    break
            elif matrix[row][col] == 'D':
                hit_points = sum(find_digits(row, col)) * 2
                players[name] -= hit_points
                if players[name] <= 0:
                    is_winner = True
                    winner = name
                    break
            elif matrix[row][col] == 'T':
                hit_points = sum(find_digits(row, col)) * 3
                players[name] -= hit_points
                if players[name] <= 0:
                    is_winner = True
                    winner = name
                    break
            elif matrix[row][col] == 'B':
                is_winner = True
                winner = name
                break
    if is_winner:
        break
    turns += 1
name = winner
print(f"{name} won the game with {turns} throws!")
