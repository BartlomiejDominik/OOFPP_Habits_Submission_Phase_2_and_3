import time
from menu.initialisation import StartInitialisation
from utilities.utilities import Utilities
from unit_test.dataset_for_test import Set
from datetime import datetime, timedelta
from functionalities.add_new_habit import AddNewHabit
from functionalities.habits_check_off import CheckOff
import os


class TestFixture:
    """A test fixture class for automated testing of the HabiBart application's functionalities.

    Attributes:
        N/A
    """

    def test_fixture(self):
        """Run a series of automated tests on the HabiBart application's functionalities.

        Args:
            N/A

        Returns:
            None
        """
        user_choice = input('\nTo start text_fixture type (t) or enter to continue.\n')
        if user_choice == "t":
            # delete the files for the next run

            # Specify the filenames you want to delete
            files_to_delete = ["test_database.json", "test_log_out_time.json"]
            script_directory = os.path.dirname(os.path.abspath(__file__))

            # Loop through the files and delete them
            for file_to_delete in files_to_delete:
                file_path = os.path.join(script_directory, file_to_delete)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    # print(f"{file_to_delete} has been deleted.")
                else:
                    print(f"{file_to_delete} does not exist.")
            model = Utilities()
            model.clear_console()
            input('\nTest_fixture is started please press enter to go forward.\n')
            # testing if the 'start_initialisation' function find the 'database' and 'log_out_file' files and because
            # there are not existing creat the new test_database and test_log_out_files with default files.
            model = Utilities()
            model.clear_console()
            print('\n########## Test 1. Creating a new data file with the default habits ##########\n')
            time.sleep(3)
            model = Utilities()
            database = "unit_test/test_database.json"
            log_out_file = "unit_test/test_log_out_time.json"
            start_init = StartInitialisation()
            start_init.start_initialisation(database, log_out_file)
            # test if "database.json" and "test_log_out_time.json" were created
            assert model.read_from_json_file(database) is not None
            assert model.read_from_json_file(log_out_file) is not None
            print('\n########## Test 1. Successfully completed! ##########\n')
            time.sleep(1.5)
            model.clear_console()
            # creat, based on five default habits, the dataset with random check_offs for last 28 days(four weeks).
            print('\n########## Test 2. Creating the dataset with random check_offs for last 28 days(four weeks) '
                  '##########\n')
            time.sleep(3)
            dataset = Set()
            dataset.test_function(model.read_from_json_file(database), database)
            result_habits = model.read_from_json_file(database)
            # check if random check_off's were added to a database
            assert any(len(habit['Check_offs']) != 0 for habit in result_habits)

            print('\n########## Test 2. Successfully completed! ##########\n')
            time.sleep(2)
            # check if adding a new habit 'Example' with class 'Habit' is working properly.
            model = Utilities()
            model.clear_console()
            print("\n########## Test 3. Adding a new habit 'Example' with class 'Habit' to check if it's working "
                  "properly. ##########\n")
            time.sleep(3)
            add_new_habit = AddNewHabit()
            new_habit = add_new_habit.add_new_habit("Example", "Longest streak run",
                                                    "daily", database, result_habits)
            print(new_habit)
            time.sleep(3)
            habits = model.read_from_json_file(database)
            assert any(task_dict['Task'] == 'Example' for task_dict in habits)
            print()
            for habit in habits:
                print(habit)
            time.sleep(3)
            print('\n########## Test 3. Successfully completed! ##########\n')
            time.sleep(3)
            model.clear_console()
            # check if check_off's id adding properly.
            print("\n########## Test 4. Check if habit is checked_off properly.  ##########\n")
            check_off = CheckOff()
            habit_task_to_find = 'Example'
            # Find the dictionary with the specified 'Task'
            found_habit = None
            for habit in habits:
                if habit['Task'] == habit_task_to_find:
                    # print(habit)
                    habits, _ = check_off.check_off_habit(habit, habits, database)
            for habit in habits:
                print(habit)
            time.sleep(3)
            # habits[5]['Check_offs'] = []
            assert len(habits[5]['Check_offs']) != 0
            print('\n########## Test 4. Successfully completed! ##########\n')
            time.sleep(3)
            model.clear_console()
            # add check off for the last 28 days to get the longest periodicity for the habit 'Example'
            print("\n########## Test 5. Add check offs for last 28 days to 'Example' habit to see if analytic "
                  "works correctly."
                  "##########\n")
            # Create a list of dates for the last 28 days
            database = 'unit_test/test_database.json'
            model = Utilities()
            habits = model.read_from_json_file(database)
            last_28_days = [datetime.now() - timedelta(days=i) for i in range(0, 28)]
            # Format the dates in the desired format
            formatted_dates = sorted([date.strftime("%Y-%m-%dT%H:%M:%S.%f") for date in last_28_days])
            habits[5]['Check_offs'] = formatted_dates
            assert len(habits[5]['Check_offs'])
            model.save_into_json_file(habits, database)
            habits = model.read_from_json_file(database)
            for habit in habits:
                print(habit)
            # print(habits[5])
            time.sleep(3)
            from functionalities.longest_run_streak import RunStreak
            run_streak = RunStreak()
            database = 'unit_test/test_database.json'
            run_streak.the_longest_run_streak_for_habits(database)
            print('\n########## Test 5. Successfully completed! ##########\n')
            input('\nAll tests are completed successfully!!! Please press Enter to launch the application.\n')

            pass

        else:
            # launch main_menu
            model = Utilities()
            model.clear_console()
            return
