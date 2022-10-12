import re
text = input()

pairs = re.finditer(r"(#+|@+)(?P<color>[a-z]{3,})(#+|@+)[\W]+(?P<amount>[\d]+)", text)
for groups in pairs:
    test = groups.group()
    words = re.findall(r"[a-z]+", test)
    digits = re.findall(r"[\d]+", test)

    print(f"You found {''.join(digits)} {''.join(words)} eggs!")

