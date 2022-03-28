

kids_count = 0
adult_count = 0
while True:
    command = input()
    if command == "Christmas":
        break
    else:
        age = int(command)
        if age <= 16:
            kids_count +=1
        else:
           adult_count +=1
toys_money = kids_count * 5
sweaters_money = adult_count * 15
print(f"Number of adults: {adult_count}" )
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {toys_money}")
print(f"Money for sweaters: {sweaters_money}")
