class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):

        return f'[{", ".join(self.data[::-1])}]'

a = Stack()
a.push('aaaa')
a.push('aaaa')
a.push('aaaa')
a.push('aaaa')
print(a.__str__())