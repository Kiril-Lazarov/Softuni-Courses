n = int(input())
longest_intersection = {}
length = []
for i in range(n):
    first_range, second_range = input().split("-")
    first_range = first_range.split(',')
    second_range = second_range.split(',')

    first_seq = set(range(int(first_range[0]), int(first_range[1])+1))
    second_seq = set(range(int(second_range[0]), int(second_range[1])+1))
    intersection = list(first_seq.intersection(second_seq))
    length.append(len(intersection))
    if len(intersection) not in longest_intersection:
        longest_intersection[len(intersection)] = intersection

longest_intersection = {k: v for k, v in sorted(longest_intersection.items(), key= lambda x: x[0], reverse= True)}
max_length = max(length)
print(f"Longest intersection is {longest_intersection[max_length]} with length {max_length}")


