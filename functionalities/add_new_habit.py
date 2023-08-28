from utilities.utilities import Utilities
import time
from habit.habit import Habit


class AddNewHabit:
    def new_habit_add(self, database, main_menu):
        model = Utilities()
        try:

            new_habit_task = ""
            while not new_habit_task:  # to check if input() in empty
                print('\nTo add a new habit please enter the following information.\n'
                      '\nTo brake and go back to main menu enter (b)\n')
                new_habit_task = input('Please insert short task description for the new habit: ')
                # .clear_console()
                model.clear_console()
        except Exception as e:
            print('An error occurred:', e)

        if new_habit_task == 'b':
            model.clear_console()
            main_menu()
        new_habit_specification = input('\nPlease insert the specification of the new habit: ')
        new_habit_periodicity = input('Please input periodicity; "w" for weakly or "d" for daily: ')

        while new_habit_periodicity != "w" and new_habit_periodicity != "d":
            print('Incorrect input! Please input periodicity; "w" for weekly or "d" for daily: ')
            model.clear_console()
            new_habit_periodicity = input('\nPlease input periodicity; "w" for weakly or "d" for daily: ')

        if new_habit_periodicity == 'w':
            new_habit_periodicity = 'weekly'
        elif new_habit_periodicity == "d":
            new_habit_periodicity = 'daily'
        habits = model.read_from_json_file(database)
        habit = self.add_new_habit(new_habit_task, new_habit_specification, new_habit_periodicity, database, habits)

        print('\nNew habit was added to the database\n')
        print(habit)
        time.sleep(4)
        model.clear_console()
        main_menu()

    @staticmethod
    def add_new_habit(new_habit_task, new_habit_specification, new_habit_periodicity, database, habits):
        model = Utilities()
        habit = Habit(new_habit_task, new_habit_specification, new_habit_periodicity, habits)
        habits.append(habit.set_new_habit())
        model.save_into_json_file(habits, database, indent_level=4)  # "database9.json"
        return habit
