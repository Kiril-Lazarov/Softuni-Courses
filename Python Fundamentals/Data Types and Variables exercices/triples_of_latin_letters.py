n = int(input())

for first in range(n):
    letter1 = chr(int(first + 97))
    for second in range(n):
        letter2 = chr(int(second + 97))
        for third in range(n):
            letter3 = chr(int(third + 97))
            print(f'{letter1}{letter2}{letter3}')