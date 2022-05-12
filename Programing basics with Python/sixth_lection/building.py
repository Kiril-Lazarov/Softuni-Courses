floor_number = int(input())
room_number = int(input())
letter_room = ''
for floor in range( floor_number, 0, -1):
    for room in range(room_number):
        if floor == floor_number:
            letter_room = 'L'
        elif floor % 2 == 0:
            letter_room = 'O'
        else:
            letter_room = 'A'
        print(f'{letter_room}{floor}{room}', end=' ')
    print()

