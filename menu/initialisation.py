from utilities.utilities import Utilities
from habit.modifications import Operations
from datetime import datetime, timedelta


class StartInitialisation:

    @staticmethod
    def start_initialisation(database, log_out_file):

        model = Utilities()
        operation = Operations()
        habits = []
        try:
            habits = model.read_from_json_file(database)  # "database(*).json"
            # main_menu()

        except FileNotFoundError:
            # If the file doesn't exist, create it with an empty "habits" list and fill it with predefined_habits()
            habits = []
            print("\nError: Database hasn't existed yet or the App wasn't able to open the existing file.\n"
                  "For that reason the database was created with following, default habits.\n")
            operation.predefined_habits(habits, database)  # why self is not working
            for habit in habits:
                print(habit)  # print each item from the list in a separate line

            input("\nPress enter to go forward.\n")
            model.clear_console()
        # checking if the logout_time file exists and if not creat a new one with the last logout date set to two days
        # before for testing purpose
        try:
            model.read_from_json_file(log_out_file)  # "database(*).json"

        except FileNotFoundError:
            # If the file doesn't exist, create new with the logout time set for testing not completed
            # habits two days before since the last login
            log_out_time = (datetime.now().date() - timedelta(days=2)).isoformat()  # .isoformat() converts date into a
            # string(ISO8601:"YYYY-MM-DD")
            model.save_into_json_file(log_out_time, log_out_file,
                                      indent_level=4)  # indent specifies number of spaces for each
            # Level of indentation in *.json file. This makes the structure of the file more readable if open
            # separately.
            print(f"\nError: Log_out_time file hasn't existed yet or the App wasn't able to open the existing file.\n"
                  f"For that reason the new file was created with following date: {log_out_time}\n")
            input("\nPress enter to go forward.\n")
            model.clear_console()
