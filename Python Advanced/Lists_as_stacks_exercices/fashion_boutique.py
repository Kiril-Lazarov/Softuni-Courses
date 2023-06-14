clothes = list(map(int, input().split(' ')))
capacity = int(input())
racks = 1
num = capacity

while clothes:
    if clothes[-1] == capacity:
        if clothes[-1] != clothes[0]:
            racks += 1
        capacity = num
        clothes.pop()
    elif clothes[-1] < capacity:
        a = clothes.pop()
        capacity -= a
    elif clothes[-1] > capacity:
        capacity = num
        racks +=1
print(racks)
