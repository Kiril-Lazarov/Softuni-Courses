number_lines = int(input())
# bracket_list = []
# full_list = []
# check_list = [')', '(']
# check_counter = 0
# isBalanced = True
# previous_open = ''
# for i in range(number_lines):
#     character = input()
#     if character == '( ':
#         character = '('
#     full_list.append(character)
#     if character == '(' or character == ')':
#         bracket_list.append(character)
# closed_brackets = bracket_list.count(')')
# if bracket_list[0] == ')':
#     isBalanced = False
# for j in range(len(bracket_list)-1):
#     if check_list == bracket_list[j:j +2]:
#         check_counter +=1
# if check_counter != (closed_brackets-1):
#     isBalanced = False
# for k in range(len(full_list)):
#     if previous_open == '(':
#         break
#     if full_list[k] == '(':
#         previous_open = '('
pair_brackets = 0
two_opened = ['(', '(']
closed_opened = []
full_list = []
isBalanced = True
previous_closed = ''
closed_counter = 0
open_counter = 0
for i in range(number_lines):
    character = input()
    if character == '( ':
        character = '('
    full_list.append(character)
    if character == '(' or character == ')':
        closed_opened.append(character)
for j in range(len(full_list)-1):
    if two_opened == full_list[j:j+2]:
        isBalanced = False
for k in range(len(closed_opened) -1):
    if two_opened == closed_opened[k:k+2]:
        isBalanced = False
        break
for l in range(len(closed_opened)):
    if closed_opened[l] == ')':
        if previous_closed == ')':
            isBalanced = False
            break
        previous_closed = ')'
    else:
        previous_closed = ''
for m in range(len(closed_opened)):
    if closed_opened[m] == ')':
        closed_counter +=1
    else:
        open_counter +=1
if closed_counter != open_counter:
    isBalanced = False





if isBalanced:
    print('BALANCED')
else:
    print('UNBALANCED')










