def rectangle(*args):
    length, hight = args

    def area():
        return length * hight

    def perimeter():
        return (length + hight) * 2

    if isinstance(length, int) and isinstance(hight, int):
        return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'

    else:
        return "Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))
