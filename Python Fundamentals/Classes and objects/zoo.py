# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#             self.mammals.append(name)
#         elif species == 'fish':
#             self.fishes.append(name)
#         elif species == 'bird':
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ''
#         if species == 'mammal':
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == 'fish':
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == 'bird':
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
#
# for i in range(count):
#     animal = input().split(' ')
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#             self.mammals.append(name)
#         elif species == 'fish':
#             self.fishes.append(name)
#         elif species == 'bird':
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ''
#         if species == 'mammal':
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == 'fish':
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == 'bird':
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
# name_of_zoo = input()
# count = int(input())
#
# zoo = Zoo(name_of_zoo)
#
# for i in range(count):
#     command = input().split(' ')
#     zoo.add_animal(command[0], command[1])
# info = input()
# print(zoo.get_info(info))

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        a = []
        word = ''
        if species == "mammal":
            a = self.mammals
            word = "Mammals"
        elif species == "fish":
            a = self.fishes
            word = "Fishes"
        elif species == "bird":
            a = self.birds
            word = "Birds"
        return f"{word} in {self.name}: {', '.join(a)}\nTotal animals: {self.__animals}"


zoo = Zoo(input())
for i in range(int(input())):
    info = input().split(' ')
    zoo.add_animal(info[0], info[1])
print(zoo.get_info(input()))
