b = tuple(map(float, input().split(" ")))
occurrences_dict = {}
for number in b:
    if number not in occurrences_dict:
        print(f"{number} - {b.count(number)} times")
        occurrences_dict[number] = b.count(number)
