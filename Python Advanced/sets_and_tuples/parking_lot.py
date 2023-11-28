n = int(input())
parking_lot = set()
for _ in range(n):
    command, string = input().split(', ')
    if command == "IN":
        parking_lot.add(string)
    else:
        if string in parking_lot:
            parking_lot.remove(string)
if parking_lot:
    for x in parking_lot:
        print(x)
else:
    print("Parking Lot is Empty")

