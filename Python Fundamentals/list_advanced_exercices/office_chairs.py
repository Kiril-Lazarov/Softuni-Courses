n = int(input())
total_diff = 0
isNeeded = True
for i in range(1,n +1):
    chairs = input().split(' ')
    chair_numbers = len(chairs[0])
    diff = abs(int(chairs[1]) - chair_numbers)
    if int(chairs[1]) > chair_numbers:
        print(f"{diff} more chairs needed in room {i}")
        isNeeded = False
    else:
        total_diff += diff
if isNeeded:
    print(f"Game On, {total_diff} free chairs left")

