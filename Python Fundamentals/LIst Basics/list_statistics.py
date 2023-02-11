n = int(input())
positives = []
negatives = []
pos_count = 0
neg_sum = 0
for i in range(n):
    num = int(input())
    if num  >= 0:
        positives.append(num)
        pos_count += 1
    else:
        negatives.append(num)
        neg_sum += num
print(positives)
print(negatives)
print(f"Count of positives: {pos_count}")
print(f"Sum of negatives: {(neg_sum)}")