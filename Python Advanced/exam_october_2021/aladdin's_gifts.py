from collections import deque

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])
gifts = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}
gifts_pairs = {'Gemstone-Porcelain Sculpture': 0, 'Gold-Diamond Jewellery': 0}


def check_gifts():
    materials.pop()
    magic_level.popleft()
    if 100<= sum <= 199:
        gifts['Gemstone'] += 1
        gifts_pairs['Gemstone-Porcelain Sculpture'] += 1
    elif 200<=sum <= 299:
        gifts['Porcelain Sculpture'] += 1
        gifts_pairs['Gemstone-Porcelain Sculpture'] += 1
    elif 300<= sum <= 399:
        gifts['Gold'] += 1
        gifts_pairs['Gold-Diamond Jewellery'] += 1
    elif 400<=sum<=499:
        gifts['Diamond Jewellery'] += 1
        gifts_pairs['Gold-Diamond Jewellery'] += 1


while True:
    sum = materials[-1] + magic_level[0]
    if 100 <= sum <= 499:

        check_gifts()
        if not materials:
            break
        if not magic_level:
            break

    else:
        if sum < 100:
            if sum % 2 == 0:
                sum = materials[-1] * 2 + magic_level[0]*3
                if not 100 <= sum <= 499:
                    materials.pop()
                    magic_level.popleft()
                else:
                    check_gifts()
                if not materials:
                    break
                if not magic_level:
                    break

            else:
                sum *= 2
                if not 100 <=sum <=499:
                    materials.pop()
                    magic_level.popleft()
                else:
                    check_gifts()
                if not materials:
                    break
                if not magic_level:
                    break

        elif sum > 499:
            sum /= 2
            if not 100 <= sum <= 499:
                materials.pop()
                magic_level.popleft()
            else:
                check_gifts()
            if not materials:
                break
            if not magic_level:
                break

if gifts_pairs['Gemstone-Porcelain Sculpture'] >= 2 or gifts_pairs['Gold-Diamond Jewellery'] >=2:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])} ')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')
sorted_gifts = {k:v for k, v in sorted(gifts.items(), key= lambda x: x[0])}
for key, value in sorted_gifts.items():
    if value == 0:
        continue
    else:
        print(f'{key}: {value}')


