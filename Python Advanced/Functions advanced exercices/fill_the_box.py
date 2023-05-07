def fill_the_box(*args):
    last_index = args.index('Finish')
    volume = args[0] * args[1] * args[2]
    sequence = args[3:last_index]
    for num in sequence:
        if volume - num<=0:
            box_left = sum(sequence[sequence.index(num) + 1:]) + abs(volume-num)
            return f'No more free space! You have {box_left} more cubes.'
        else:
            volume -= num
    return f"There is free space in the box. You could put {volume} more cubes."

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))