import re
matrix = [input().split() for row in range(6)]
bucket_hits = []
total_points = 0

def calculate(col):
    result = 0
    for row in range(6):
        if matrix[row][col].isdigit():
            result += int(matrix[row][col])
    return result


for attempt in range(3):
    row, col = [int(x) for x in re.findall(r'\d+', input())]
    if 0<= row<6 and 0<= col<6:
        if matrix[row][col] == 'B':
            if (row, col) not in bucket_hits:
                total_points += calculate(col)
                bucket_hits.append((row, col))

if total_points >= 100:
    prize = ''
    if total_points >= 300:
        prize = 'Lego Construction Set'
    elif total_points >= 200:
        prize = 'Teddy Bear'
    elif total_points >=100:
        prize = 'Football'

    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    diff = 100 -total_points
    print(f"Sorry! You need {diff} points more to win a prize.")