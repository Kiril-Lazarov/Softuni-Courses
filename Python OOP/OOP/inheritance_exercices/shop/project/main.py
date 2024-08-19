from task_for_classes.project import ProductRepository
from task_for_classes.project import Drink
from task_for_classes.project import Food

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
