def cache(func):
        dictionary = {}
        def wrapper(n):
            if n in dictionary:
                return dictionary[n]
            result = func(n)
            dictionary[n] = result
            return result
        wrapper.log = dictionary
        return wrapper
@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
