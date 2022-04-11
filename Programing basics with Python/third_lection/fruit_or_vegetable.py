product_name = input()
fruit = ""

if product_name == "banana"\
        or product_name == "apple"\
        or product_name == "kiwi"\
        or product_name == "cherry"\
        or product_name == "lemon"\
        or product_name == "grapes":
    fruit = "fruit"
elif product_name == "tomato" \
        or product_name == "cucumber" \
        or product_name == "pepper"\
        or product_name == "carrot":
    fruit = "vegetable"
else:
    fruit = "unknown"
print(fruit)