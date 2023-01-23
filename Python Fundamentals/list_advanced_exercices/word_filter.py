string = input().split(' ')
print('\n'.join([i for i in string if len(i) % 2 == 0]))