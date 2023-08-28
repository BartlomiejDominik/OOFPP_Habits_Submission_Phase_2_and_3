from datetime import datetime


# Class prepared for adding a new habit


class Habit:

    def __init__(self, task, specification, periodicity, habits):
        self.task = task
        self.specification = specification
        self.periodicity = periodicity
        self.habits = habits

    def set_new_habit(self):
        start_date = datetime.now().date()
        id_number = max((habit['Id'] for habit in self.habits), default=0) + 1

        return {'Id': id_number, 'Task': self.task, 'Specification': self.specification,
                'Periodicity': self.periodicity, 'Active': True, 'Start_Date': start_date, 'Check_offs': []}

    def __str__(self):
        return f"Task: {self.task}\nSpecification: {self.specification}\nPeriodicity: {self.periodicity}"

    ################################################################################################################

