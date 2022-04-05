high = int(input())
lenght = int(input())

cake_pieces = high * lenght
pieces_sum = 0
took_pieces = input()
while True:

    if took_pieces != "STOP":
        cake_pieces -= int(took_pieces)
        pieces_sum += int(took_pieces)
        if cake_pieces > 0:
            took_pieces = input()
        else:
            print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
            break
    else:
        print(f"{cake_pieces} pieces are left." )
        break
