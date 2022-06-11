limit_hundreds = int(input())
limit_decades = int(input())
limit_integers = int(input())

integers = 0
dec = 0
hun = 0
for i1 in range(1, limit_hundreds + 1):
    if i1 % 2 == 0:
        integers = i1
        for x in range(1, 8):
            for i2 in range(2, limit_decades + 1):
                if i2 % x == 0 and i2 // x == i2:
                    if i2 == 4 or i2 == 6 or i2 == 9 or i2 == 8:
                        pass
                    else:
                        dec = i2
                        for i3 in range(1, limit_integers + 1):
                            if i3 % 2 == 0:
                                hun = i3
                                print(i1, i2, i3)