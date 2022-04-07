animal = input("")

type_animal = ""

if animal == "crocodile"\
    or animal == "tortoise"\
    or animal == "snake":
    type_animal = "reptile"
elif animal == "dog":
    type_animal = "mammal"
else:
    type_animal = "unknown"
print(type_animal)