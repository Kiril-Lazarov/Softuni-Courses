# quantity_detergent_bottles = int(input()) * 750
#
# used_detergent = 0
# loading = 0
# plate = 5
# saucepan = 15
# plate_count = 0
# saucepan_count = 0
#
# while True:
#     if quantity_detergent_bottles >= 0:
#         quantity_vessels = input()
#         loading += 1
#         if quantity_vessels != "End":
#             if loading % 3 != 0:
#                 quantity_detergent_bottles -= int(quantity_vessels) * plate
#                 plate_count += int(quantity_vessels)
#             else:
#                 quantity_detergent_bottles -= int(quantity_vessels) * saucepan
#                 saucepan_count += int(quantity_vessels)
#         else:
#
#             if quantity_detergent_bottles >= 0:
#                 print("Detergent was enough!")
#                 print(f"{plate_count} dishes and {saucepan_count} pots were washed.")
#                 print(f"Leftover detergent {quantity_detergent_bottles} ml.")
#                 break
#             else:
#                 print(f"Not enough detergent, {abs(quantity_detergent_bottles)} ml. more necessary!")
#                 break
#     else:
#         if quantity_detergent_bottles == 0:
#             print("Detergent was enough!")
#             print(f"{plate_count} dishes and {saucepan_count} pots were washed.")
#             print(f"Leftover detergent {quantity_detergent_bottles} ml.")
#             break
#         else:
#             print(f"Not enough detergent, {abs(quantity_detergent_bottles)} ml. more necessary!")
#             break
#
#  Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала
# [1…10]
# На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи,
# брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]

bottles = int(input())
chem_quantity = bottles * 750
command = input()
refill_count = 0
plates = 0
saucepan = 0
while command != 'End':
    count_items = int(command)
    refill_count += 1
    if refill_count % 3 == 0:
        saucepan += count_items
        current_quantity = count_items * 15
    else:
        plates += count_items
        current_quantity = count_items * 5
    chem_quantity -= current_quantity
    if chem_quantity < 0:
        break
    command = input()
if chem_quantity >= 0:
    print("Detergent was enough!")
    print(f"{plates} dishes and {saucepan} pots were washed.")
    print(f"Leftover detergent {abs(chem_quantity)} ml.")
else:
    print(f"Not enough detergent, {abs(chem_quantity)} ml. more necessary!")
