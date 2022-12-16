names = input().split(', ')
sorted_name = sorted(names)
sorted_name = sorted(sorted_name, key=lambda x: -len(x))
print(sorted_name)

