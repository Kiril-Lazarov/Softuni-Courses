M = int(input())
control_value = 0
combinations_counter = 0
final_pass = ''
isFounded = False
isFourth = False
a = 0
b = 0
c = 0
d = 0
for i1 in range(1, 10):
    a = i1
    for i2 in range(1, 10):
        b = i2
        for i3 in range(1, 10):
            c = i3
            for i4 in range(1, 10):
                d = i4
                control_value = a * b + c * d
                if 4 <= control_value <= 144 and control_value == M:
                    if a < b and c > d:
                        combinations_counter += 1
                        isFounded = True
                        print(f'{a}{b}{c}{d}', end=' ')
                        if combinations_counter == 4:
                            isFourth = True
                            final_pass = str(f'{a}{b}{c}{d}')
print()
if not isFounded or not isFourth:
    print('No!')
else:
    print(f'Password: {final_pass}')