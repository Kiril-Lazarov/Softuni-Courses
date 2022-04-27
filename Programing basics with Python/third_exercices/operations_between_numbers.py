number1 = int(input())
number2 = int(input())
operator = input()
result = 0
is_even = ''
abc = 0
remainder = 0

if operator == '+':
    abc = 1
    result = number1 + number2
elif operator == '-':
    abc = 1
    result = number1 - number2
elif operator == '*':
    abc = 1
    result = number1 * number2
elif operator == '/' and number2 != 0:
    abc = 2
    result = number1 / number2
if number2 == 0:
    abc = 3
    result = result

elif operator == '%':
    abc = 4
    result = number1 % number2
if abc == 1:
    if result % 2 == 0:
        is_even = 'even'
    else:
        is_even = 'odd'
    print(f"{number1} {operator} {number2} = {result} - {is_even}")
elif abc == 2:
    print(f"{number1} / {number2} = {result:.2f}")
elif abc == 3:
    print(f"Cannot divide {number1} by zero")
elif abc == 4:
    print(f"{number1} % {number2} = {result}")
