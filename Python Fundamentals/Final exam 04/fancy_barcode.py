# import re
#
# n = int(input())
#
# for i in range(n):
#     text = input()
#     code = re.findall(r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+", text)
#     if len(code) != 0:
#         numbers = re.findall(r'[\d]+', ''.join(code))
#         if len(numbers) == 0:
#             print('Product group: 00')
#         else:
#             print(f"Product group: {''.join(numbers)}")
#     else:
#         print("Invalid barcode")
import re

n = int(input())
for i in range(n):
    text = input()
    symbols = re.findall(r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+", text)

    if len(symbols) == 0:
        print("Invalid barcode")
    else:
        nums = "".join(list(map(str, re.findall(r'[0-9]', ''.join(symbols)))))
        if len(nums) == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {nums}")
