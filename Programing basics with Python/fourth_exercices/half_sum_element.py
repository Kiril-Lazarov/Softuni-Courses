# import sys
#
# count_of_numbers = int(input())
# sum_of_numbers = 0
# max_num = - sys.maxsize
#
# for number in range(count_of_numbers):
#     current_number = int(input())
#     sum_of_numbers += current_number
#     if max_num < current_number:
#         max_num = current_number
# if sum_of_numbers - max_num == sum_of_numbers / 2:
#     print('Yes')
#     print(f"Sum = {max_num}")
# else:
#     print('No')
#     print(f'Diff = {abs(sum_of_numbers - 2 * max_num)}')

# •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# •	След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на продукт, чиято стойност е по-висока от наличния бюджет) :
# o	Име на продукта – текст
# o	Цена на продукта – реално число в интервала [1.00… 5000.00]

# budget = float(input())
# command = input()
# items = 0
# sum = 0
# price = 0
# while True:
#     if command == "Stop":
#         break
#     price = float(input())
#     items += 1
#     if items % 3 == 0:
#         price /= 2
#     budget -= price
#     if budget < 0:
#         break
#     sum += price
#     command = input()
# if command == "Stop":
#     print(f"You bought {items} products for {sum:.2f} leva.")
# elif budget < 0:
#     print("You don't have enough money!")
#     print(f"You need {abs(budget):.2f} leva!")
#
# От конзолата се четат по два реда до въвеждане на команда "END", ако са минали повече от 5 дни в изкачване или се достигне върха (8 848м):
# •	"Yes" / "No" - текст - дали Атанас ще нощува преди изкачването на следващите метри или не
# •	Изкачени метри - цяло число в интервала [1...4000]




