from task_for_classes.project import Car

class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)