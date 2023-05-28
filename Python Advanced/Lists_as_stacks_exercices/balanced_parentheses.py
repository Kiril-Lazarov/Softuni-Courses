parenthesis = input()

open = '([{'
closed = ')}]'
series = []
pairs = {
    "(": ")",
    "[": ']',
    "{": "}"
}
for char in parenthesis:
    if char in open:
        series.append(char)
    elif char in closed:
        if len(series) == 0:
            series.append(char)
            break
        elif pairs[series[-1]] == char:
            series.pop()
if len(series) == 0:
    print("YES")
else:
    print('NO')
