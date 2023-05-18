def operate(operator, *args):
    def add(args):

        return sum(args)

    def subtract(args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(args):
        result = args[0]
        for num in args[1:]:
            if num != 0:
                result /= num
        return result

    if operator == '+':
        return add(args)
    elif operator == '-':
        return subtract(args)
    elif operator == "*":
        return multiply(args)
    else:
        return divide(args)


print(operate("*", 9, 8, 3))
print(operate("/", 3, 5,2))