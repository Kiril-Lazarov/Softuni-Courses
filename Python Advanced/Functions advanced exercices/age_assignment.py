def age_assignment(*args, ** kwargs):
    result = []
    kwargs = {k:v for k,v  in sorted(kwargs.items(), key=lambda x: x[0])}
    for letter, age in kwargs.items():
        for name in args:
            if letter == name[0]:
                result.append(f'{name} is {age} years old.')
    return '\n'.join(result)



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))