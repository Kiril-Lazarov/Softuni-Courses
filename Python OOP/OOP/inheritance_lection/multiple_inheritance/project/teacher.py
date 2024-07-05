from person import Person
from task_for_classes.project import Employee


class Teacher(Employee,Person):
    def teach(self):
        return 'teaching...'

