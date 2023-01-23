sequence = input().split(', ')
words = input()
final = [sequence[i] for i in range(len(sequence)) if sequence[i] in words]
print(final)