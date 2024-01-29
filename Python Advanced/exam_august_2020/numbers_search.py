def numbers_searching(*args):
    missing_value = 0
    duplicate_numbers = []
    min_value = min(args)
    max_value = max(args)
    n = max_value - min_value
    for num in range(min_value, max_value +1):
        if num not in args:
            missing_value = num
        if args.count(num) >= 2:
            duplicate_numbers.append(num)

    return [missing_value, sorted(duplicate_numbers)]




print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))