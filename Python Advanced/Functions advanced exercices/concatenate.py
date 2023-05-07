def concatenate(*args, **kwargs):
    expression = ''.join(args)

    for key, value in kwargs.items():
        if key in expression:
          expression = expression.replace(key, value)
    return expression



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))