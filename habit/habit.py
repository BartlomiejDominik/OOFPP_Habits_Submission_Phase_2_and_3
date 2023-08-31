from datetime import datetime

class Habit:
    """A class for adding a new habit.

    Args:
        task (str): The name of the habit/task.
        specification (str): Additional details or description of the habit.
        periodicity (str): The periodicity of the habit (e.g., daily, weekly).
        habits (list): List of existing habits.

    Attributes:
        task (str): The name of the habit/task.
        specification (str): Additional details or description of the habit.
        periodicity (str): The periodicity of the habit (e.g., daily, weekly).
        habits (list): List of existing habits.
    """

    def __init__(self, task, specification, periodicity, habits):
        self.task = task
        self.specification = specification
        self.periodicity = periodicity
        self.habits = habits

    def set_new_habit(self):
        """Create a new habit with provided details.

        Returns:
            dict: A dictionary representing the new habit.
        """
        start_date = datetime.now().date()
        id_number = max((habit['Id'] for habit in self.habits), default=0) + 1

        return {'Id': id_number, 'Task': self.task, 'Specification': self.specification,
                'Periodicity': self.periodicity, 'Active': True, 'Start_Date': start_date, 'Check_offs': []}

    def __str__(self):
        """
        String representation of the Habit object.

        Returns:
            str: A formatted string displaying habit details.
        """
        return f"Task: {self.task}\nSpecification: {self.specification}\nPeriodicity: {self.periodicity}"
