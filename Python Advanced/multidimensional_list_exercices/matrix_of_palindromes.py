rows, cols = [int(x) for x in input().split()]

palindromes_m = []
buffer = []


def ascii_translator(rows):
    letter = chr(rows + 97)
    return letter


def find_letters(rows, cols):
    string = ''
    first = ascii_translator(rows)
    string += first + ascii_translator(rows + cols) + first
    return string


for i in range(rows):
    for j in range(cols):
        buffer.append(find_letters(i,j))
    palindromes_m.append(buffer)
    buffer = []





for i in range(rows):
    print(' '.join(palindromes_m[i]))
