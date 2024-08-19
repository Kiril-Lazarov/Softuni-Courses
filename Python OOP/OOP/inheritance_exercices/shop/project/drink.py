from task_for_classes.project import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10
    def __init__(self, name):
        super().__init__(name, self.DEFAULT_QUANTITY)

