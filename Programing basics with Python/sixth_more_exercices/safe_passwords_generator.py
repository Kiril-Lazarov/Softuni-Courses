# a = int(input())
# b = int(input())
# max_passwords = int(input())
#
# symbol1 = ''
# symbol2 = ''
# symbol3 = 0
# symbol4 = 0
# pass_counter = 0
# count_A = 35
# count_B = 64
# isDone = False
#
# if max_passwords > 0:
#     if a * b < max_passwords:
#         for x in range(1, a + 1):
#             symbol3 = x
#             for y in range(1, b + 1):
#                 symbol4 = y
#                 if count_A <= 55:
#                     symbol1 = chr(count_A)
#                     count_A += 1
#                 else:
#                     count_A = 35
#                     symbol1 = chr(count_A)
#                 if count_B <= 96:
#                     symbol2 = chr(count_B)
#                     count_B += 1
#                 else:
#                     count_B = 64
#                     symbol2 = chr(count_B)
#
#                 print(f'{symbol1}{symbol2}{symbol3}{symbol4}{symbol2}{symbol1}', end='|')
#
#     else:
#         for x in range(1, a + 1):
#             symbol3 = x
#             for y in range(1, b + 1):
#                 symbol4 = y
#                 if count_A <= 55:
#                     symbol1 = chr(count_A)
#                     count_A += 1
#                 else:
#                     count_A = 35
#                     symbol1 = chr(count_A)
#                 if count_B <= 96:
#                     symbol2 = chr(count_B)
#                     count_B += 1
#                 else:
#                     count_B = 64
#                     symbol2 = chr(count_B)
#                 print(f'{symbol1}{symbol2}{symbol3}{symbol4}{symbol2}{symbol1}', end='|')
#                 pass_counter += 1
#                 if pass_counter == max_passwords:
#                     isDone = True
#                     break
#             if isDone:
#                 break
def password(c):
    sym_a = '#'
    sym_b = '@'
    num_x = a
    num_y = b
    password = ''
    num_iterations = 0
    for i in range(1, a+1):
        num_x = i
        for j in range(1, b+1):
            num_y = j
            if ord(sym_a) > 55:
                sym_a = '#'
            if ord(sym_b) > 96:
                sym_b = '@'
            password = f'{sym_a}{sym_b}{num_x}{num_y}{sym_b}{sym_a}|'
            sym_a = chr(ord(sym_a) + 1)
            sym_b = chr(ord(sym_b) + 1)
            num_iterations +=1
            print(password, end ='')
            if num_iterations == max_passwords:
                break
        if num_iterations == max_passwords:
            break

a = int(input())
b = int(input())
max_passwords = int(input())
c = a * b

if a * b < max_passwords:
    password(c)
else:
    password(max_passwords)

