n = int(input())
odd = []
even = []
positive = []
negative = []
for i in range(n):
    integer = int(input())
    if integer % 2 == 0:
        even.append(integer)
    else:
        odd.append(integer)
    if integer >= 0:
        positive.append(integer)
    else:
        negative.append(integer)
command = input()
print(eval(command))
