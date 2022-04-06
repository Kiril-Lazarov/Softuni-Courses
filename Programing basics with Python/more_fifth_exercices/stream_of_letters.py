symbol = input()
c_count = 0
o_count = 0
n_count = 0
key_count = 0
word = ''

while symbol != 'End':
    isPrint = True
    if 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
        if symbol == 'c' and c_count == 0:
            c_count += 1
            key_count += 1
            isPrint = False
        elif symbol == 'o' and o_count == 0:
            o_count += 1
            key_count += 1
            isPrint = False
        elif symbol == 'n' and n_count == 0:
            n_count += 1
            key_count += 1
            isPrint = False
        if isPrint:
            word += symbol
            # print(word)
    if key_count >= 3:
        print(word, end=chr(32))
        c_count = 0
        o_count = 0
        n_count = 0
        key_count = 0
        word = ''

    symbol = input()
