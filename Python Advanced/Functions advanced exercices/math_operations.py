from collections import deque


def math_operations(*args, **kwargs):
    args_deque = deque(args)
    list = []
    i = 0
    while args_deque:
        parameter = i % 4
        number = args_deque.popleft()
        if parameter == 0:

                kwargs['a'] += number
        elif parameter == 1:

                kwargs['s'] -= number
        elif parameter == 2:
            if number != 0:
                kwargs['d'] /= number
        elif parameter == 3:

                kwargs['m'] *= number
        i += 1
    result = {k:v for k,v in sorted(kwargs.items(), key= lambda x: (-x[1], x[0]))}
    for key, value in result.items():
        list.append(f'{key}: {value:.1f}' )

    return '\n'.join(list)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))