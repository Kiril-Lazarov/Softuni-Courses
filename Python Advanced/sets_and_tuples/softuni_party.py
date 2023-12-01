n = int(input())

vip = set()
regular = set()

for i in range(n):
    ticket = input()
    if ticket[0].isdigit():
        vip.add(ticket)
    else:
        regular.add(ticket)

while True:
    ticket = input()
    if ticket == "END":
        break

    if ticket in vip:
        vip.remove(ticket)
    if ticket in regular:
        regular.remove(ticket)

print(len(vip) + len(regular))
for ticket in sorted(vip):
    print(ticket)
for ticket in sorted(regular):
    print(ticket)



