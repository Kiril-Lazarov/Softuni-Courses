from collections import deque


def list_manipulator(first, second, third, *args):
    first = deque(first)
    args = deque(args)
    command1, command2 = second, third
    if second == 'add' and third == 'beginning':
        if args:
            while args:
                first.appendleft(args.pop())



    if second == 'add' and third == 'end':
        if args:
            while args:
                first.append(args.popleft())



    if second == 'remove' and third == 'beginning':
        if args:
            for num in args:
                for _ in range(num):
                    first.popleft()
        else:
            first.popleft()

    if second == 'remove' and third == 'end':
        if args:
            for num in args:
                for _ in range(num):
                    first.pop()
        else:
            first.pop()
    return list(first)

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

