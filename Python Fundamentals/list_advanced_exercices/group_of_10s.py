sequence = list(map(int, input().split(', ')))
current_sequence = list()
level = 1
while len(sequence) > 0:
    current_sequence = [i for i in sequence if i <= level * 10]
    for k in current_sequence:
        sequence.remove(k)

    print(f"Group of {level * 10}'s: {current_sequence}")
    level += 1

