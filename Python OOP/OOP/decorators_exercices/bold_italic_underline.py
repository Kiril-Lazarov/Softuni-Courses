def make_underline(func_ref):
    def wrapper(*args):
        return  f'<u>{func_ref(*args)}</u>'
    return wrapper

def make_italic(func_ref):
    def wrapper(*args):
        return f'<i>{func_ref(*args)}</i>'

    return wrapper


def make_bold(func_ref):
    def wrapper(*args):
        result = f'<b>{func_ref(*args)}</b>'
        return result

    return wrapper



@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))




