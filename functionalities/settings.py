from utilities.utilities import Utilities
from unit_test.dataset_for_test import Set
import time
from functionalities.change_date import ChangeDate


class Settings:
    """A class to handle user settings related to habits.

    Args:
        habits (list): List of user's habits.
        main_menu (function): The main menu function for navigation.
        database (str): The path to the JSON database file containing user data.
        log_out_file (str): The path to the file storing last logout information.
    """
    def __init__(self, habits, main_menu, database, log_out_file):
        self.habits = habits
        self.main_menu = main_menu
        self.database = database
        self.log_out_file = log_out_file

    @staticmethod
    def settings(database, log_out_file):
        """Display and manage user settings related to habits.

        Args:
            database (str): The path to the JSON database file containing user data.
            log_out_file (str): The path to the file storing last logout information.
        """
        model = Utilities()
        model.clear_console()
        model = Utilities()
        dataset = Set()
        model.clear_console()
        habits = model.read_from_json_file(database)
        while True:
            try:
                user_choice = input('\n1. Deactivate existing habit\n'
                                    '\n2. To manually set the last login date for testing purpose.\n'
                                    '\nPlease choose one option from the list or (b) to back to menu:\n')
                if user_choice == '1':
                    model.clear_console()
                    print(
                        '\nTo deactivate one of the active habits, please type the number from the list and press '
                        '"enter":\n')
                    counter = 0
                    active_habits = []

                    for habit in habits:
                        if habit['Active']:
                            counter += 1
                            active_habits.append(habit)
                            print(counter, habit['Task'], habit['Start_Date'])

                    if active_habits:
                        user_choice = input(
                            '\nPlease enter the number from the list above (or press Enter to continue without '
                            'deactivating): ')

                        if user_choice.isdigit():
                            choice_index = int(user_choice) - 1
                            if 0 <= choice_index < len(active_habits):
                                selected_habit = active_habits[choice_index]
                                selected_habit['Active'] = False
                                print(f"\nYou've deactivated the habit: {selected_habit['Task']}")
                                # Save the modified habits data back to the JSON file
                                model.save_into_json_file(habits, database, indent_level=4)
                                time.sleep(4)
                                model.clear_console()

                            else:
                                model.clear_console()
                                print("Invalid choice. No habit was deactivated.")
                                time.sleep(2)
                                model.clear_console()
                                pass
                        else:
                            model.clear_console()
                            print("\nContinuing without deactivating any habit.")
                            time.sleep(2)
                            model.clear_console()
                    else:
                        model.clear_console()
                        print("No active habits to deactivate.")
                        time.sleep(2)
                        break
                elif user_choice == '2':
                    model.clear_console()
                    change_date = ChangeDate()
                    change_date.change_date(log_out_file)
                elif user_choice == 'b':
                    model.clear_console()
                    return  # main_menu
                else:
                    model.clear_console()

            except Exception as e:
                print('An error occurred:', e)
