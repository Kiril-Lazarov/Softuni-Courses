def tags(char):
    def decorator(func_ref):
        def wrapper(*args):
            return f'<{char}>{func_ref(*args)}</{char}>'
        return wrapper

    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

