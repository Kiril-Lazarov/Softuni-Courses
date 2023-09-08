lists = input().split('|')
final_list = [x.split() for x in lists]


flattened = [num for sublist in final_list[::-1] for num in sublist]
print(' '.join(flattened))
