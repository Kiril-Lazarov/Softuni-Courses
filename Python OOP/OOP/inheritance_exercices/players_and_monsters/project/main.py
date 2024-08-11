from task_for_classes.project import Elf
from task_for_classes.project import Hero
from task_for_classes.project import Knight

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
knight = Knight('j', 7)
print(str(knight))