start = input()
stop = input()
result = ''
for i in range(int(start), int(stop)+1):
    result += chr(int(i)) + ' '
print(result)