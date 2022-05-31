man_count = int(input())
woman_count = int(input())
max_table = int(input())

table_count = 0
isTableOver = False
if max_table > 0:
    for male in range(1, man_count + 1):
        for female in range(1, woman_count + 1):
            table_count += 1
            print(f'({male} <-> {female})', end=' ')
            if table_count == max_table:
                isTableOver = True
                break
        if isTableOver:
            break
