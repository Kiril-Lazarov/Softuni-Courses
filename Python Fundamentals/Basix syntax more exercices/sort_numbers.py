# import sys
# test_number = -sys.maxsize
# list1 = []
# index_to_delete = 0
# for i in range(3):
#     number = int(input())
#     list1.append(number)
# for j in range(len(list1)):
#     if list1[j]>test_number:
#         test_number = list1[j]
#         index_to_delete = j
# del list1[index_to_delete]
# print(test_number)
# test_number = -sys.maxsize
# for k in range(len(list1)):
#     if list1[k] > test_number:
#         test_number = list1[k]
#         index_to_delete = k
# del list1[index_to_delete]
# print(test_number)
# print(list1[0] )
total_sum = 0
special_discount = 1
while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    if float(command) < 0:
        print('Invalid price!')
    elif float(command) == 0:
        print("Invalid order!")
    else:
        total_sum += float(command)
if command == 'special':
    special_discount = 0.9
if total_sum == 0:
    print("Invalid order!")
else:
    total_price = total_sum * 1.2 * special_discount
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_sum:.2f}$')
    print(f'Taxes: {total_sum*0.2:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')