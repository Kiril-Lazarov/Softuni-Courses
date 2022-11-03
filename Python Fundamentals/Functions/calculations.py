def math(action, first, second):
    result = None
    if action == 'multiply':
        result = first * second
    elif action == 'divide':
        result = int(first / second)
    elif action == 'add':
        result = first + second
    elif action == 'subtract':
        result = first - second
    return result

action = input()
first = int(input())
second = int(input())

print(math(action,first, second))