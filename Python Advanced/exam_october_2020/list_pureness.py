from collections import deque


def best_list_pureness(*args):
    sequence = deque(args[0])
    rotates_num = args[-1]
    best_sum = {}
    for k in range(rotates_num+1):
        result = 0
        for index, num in enumerate(sequence):
            result += index * num
        best_sum[k] = result
        sequence.appendleft(sequence.pop())

    # print(best_sum)
    sorted_best_sum = {k:v for k, v in sorted(best_sum.items(), key= lambda x: (-x[1], x[0]))}
    # print(sorted_best_sum)
    for key, value in  sorted_best_sum.items():
        return f'Best pureness {value} after {key} rotations'
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
