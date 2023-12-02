numbers = tuple(map(int, input().split(' ')))
target = int(input())
final_pairs = set()
iterrations = 0
for i in range(len(numbers)-1):
    reduced_numbers = tuple(numbers[i+1:])
    for k in range(len( reduced_numbers)):
        iterrations +=1
        if numbers[i] +  reduced_numbers[k] == target:
            print(f'{numbers[i]} + { reduced_numbers[k]} = {target}')
            final_pairs.add((numbers[i],reduced_numbers[k]))

print(f'Iterations done: {iterrations}')
for pairs in final_pairs:
    print(pairs)