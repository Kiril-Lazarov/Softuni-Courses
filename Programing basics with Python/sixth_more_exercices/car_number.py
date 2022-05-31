start_num = int(input())
final_num = int(input())

for i1 in range(start_num, final_num + 1):
    for i2 in range(start_num, final_num + 1):
        for i3 in range(start_num, final_num + 1):
            for i4 in range(start_num, final_num + 1):
                if (i1 % 2 == 0 and i4 % 2 == 1) or (i1 % 2 == 1 and i4 % 2 == 0):
                    if i1 > i4:
                        if (i2 + i3) % 2 == 0:
                            print(f'{i1}{i2}{i3}{i4}', end=' ')
