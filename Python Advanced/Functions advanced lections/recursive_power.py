def recursive_power(number, power):
    result = 1
    if power == 0:
        return result
    result  = number ** power

    recursive_power(number, power - 1)
    return result

print(recursive_power(2, 10))
print(recursive_power(10, 100))