def ascii_sum(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i])
    return total
n = int(input())

even = set()
odd = set()

for i in range(n):
    n = i + 1
    name =ascii_sum(input())
    if (name // n) % 2 == 0:
        even.add(name//n)
    else:
        odd.add(name//n)
sum_even = sum(even)
sum_odd = sum(odd)
if sum_even == sum_odd:
    result =  even.union(odd)
elif sum_even> sum_odd:
    result = even.symmetric_difference(odd)
else:

    result = odd.difference(even)

print(*result, sep= ', ')



