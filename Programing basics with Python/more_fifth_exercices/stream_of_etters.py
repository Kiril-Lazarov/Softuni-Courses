word = ''
c_counter = 0
n_counter = 0
o_counter = 0
while True:
    letter = input()
    if letter != 'End':
        if 64 < ord(letter) < 91 or 96 < ord(letter) < 123:
            if letter == 'c':
                c_counter += 1
                if c_counter > 1:
                    word += letter
            elif letter == 'n':
                n_counter += 1
                if n_counter > 1:
                    word += letter
            elif letter == 'o':
                o_counter += 1
                if o_counter > 1:
                    word += letter
            else:
                word += letter
        else:
            continue
        if c_counter >= 1 and n_counter >= 1 and o_counter >= 1:
            print(f'{word}{chr(32)}', end='')
            word = ''
            c_counter = 0
            n_counter = 0
            o_counter = 0
    else:
        break
