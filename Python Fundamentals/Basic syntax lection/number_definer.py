num = float(input())

if num == 0:
    print("zero")
else:
    if 0 < num < 1:
        print("small positive")
    elif 1 < num < 1000000:
        print('positive')
    elif num > 1000000:
        print('large positive')
    elif -1 <= num <= 0:
        print("small negative")
    elif -1000000 <= num <= -1:
        print("negative")
    else:
        print('large negative')
