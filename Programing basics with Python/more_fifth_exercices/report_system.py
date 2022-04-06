#
#
# charity_sum = int(input())
# paid_count = 0
# cash_count = 0
# total_cash_sum = 0
# total_card_sum = 0
# card_count = 0
#
# transaction_status = False
#
# while True:
#     if charity_sum > 0:
#         paid_count += 1
#         item_price = input()
#         if item_price != "End":
#             if paid_count % 2 == 1:  # плаща се кеш
#                 if int(item_price) > 100:
#                     print("Error in transaction!")
#                 else:
#                     total_cash_sum += int(item_price)
#                     cash_count += 1
#                     charity_sum -= int(item_price)
#                     transaction_status = True
#                     print("Product sold!")
#             else:  # плаща се с карта
#                 if int(item_price) < 10:
#                     print("Error in transaction!")
#                 else:
#                     total_card_sum += int(item_price)
#                     card_count += 1
#                     charity_sum -= int(item_price)
#                     transaction_status = True
#                     print("Product sold!")
#         else:
#             print("Failed to collect required money for charity.")
#             transaction_status = False
#             break
#     else:
#         transaction_status = True
#         break
# if transaction_status == True:
#     print(f"Average CS: {total_cash_sum / cash_count:.2f}")
#     print(f"Average CC: {total_card_sum / card_count:.2f}")
#
# · Ако продуктът надвишава 100лв., за него не може да се плати в брой
#
# · Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
#
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
#
# Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
#
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства: /
# цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500

sum_needed = int(input())
command = input()
transaction_count = 1
card_payment_method = 0
cash_payment_method = 0
total_sum = 0
cash_count = 0
card_count = 0
while command != 'End':
    item_price = int(command)
    if transaction_count % 2 != 0:
        if item_price <= 100:
            cash_payment_method += item_price
            cash_count +=1
            total_sum += item_price
            print("Product sold!")

        else:
            print("Error in transaction!")
        transaction_count += 1
    else:
        if item_price < 10:
            print("Error in transaction!")
        else:
            card_payment_method += item_price
            card_count +=1
            total_sum += item_price
            print("Product sold!")
        transaction_count += 1
    if sum_needed <= total_sum:
        break
    command = input()
if sum_needed <= total_sum:
    print(f"Average CS: {cash_payment_method/cash_count:.2f}")
    print(f"Average CC: {card_payment_method/card_count:.2f}")
else:
    print("Failed to collect required money for charity.")
