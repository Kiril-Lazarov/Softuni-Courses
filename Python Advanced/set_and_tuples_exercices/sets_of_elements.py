n, m = map(int, input().split(" "))
first = set()
second = set()
for i in range(n+m):
    if i < n :
        first.add(input())
    else:
        second.add(input())

final = first.intersection(second)
for nums in final:
    print(nums)
