num = input()
final_num = 0
shot_count = 0
for i in range(9,0, -1):
    test_digit = i
    for j in range(len(num)):

        if (test_digit - int(num[j])) == 0:
            shot_count +=1
            degree = len(num)  - shot_count
            final_num += test_digit * 10 ** degree

print(final_num)
