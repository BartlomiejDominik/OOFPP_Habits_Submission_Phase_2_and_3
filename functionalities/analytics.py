from utilities.utilities import Utilities
from datetime import datetime, timedelta
from functionalities.longest_run_streak import RunStreak


class Analytics:
    """This class coordinates the analytics part of the code."""

    def __init__(self, habits, main_menu):
        """Initialize an Analytics instance.

        Args:
            habits (list): List of habit dictionaries.
            main_menu (function): Function to navigate back to the main menu.
        """
        self.habits = habits
        self.main_menu = main_menu

    @staticmethod
    def analytics(main_menu, database):
        """Navigate through the analytics submenu.

        Args:
            main_menu (function): Function to navigate back to the main menu.
            database (str): The name of the JSON database file.
        """
        model = Utilities()
        model.clear_console()
        while True:
            model.clear_console()
            print(
                '\nAvailable analytics:\n'
                '\n1. The list of all currently tracked habits sorted by their periodicity.\n'
                '\n2. The longest run streak for habits.\n')

            try:
                user_choice = input('Please choose the number from the list above or (b) to go back: ')

                if user_choice == "1":
                    model = Utilities()
                    habits = model.read_from_json_file(database)
                    habits_tuple = tuple(habits)  # The tuple() constructor is used to create a tuple from the list
                    print(habits_tuple)
                    model.clear_console()
                    print(
                        '\nThe list of all currently tracked habits sorted by their periodicity.\n')
                    # "Habits as a tuple:

                    def habits_daily(x):
                        """This function sorted out the activ habits with daily periodicity"""
                        return x['Periodicity'] == 'daily' and x['Active']  # == True

                    filtered_habits = tuple(filter(habits_daily, habits_tuple))
                    print('\nPeriodicity: daily\n')
                    for count, habit in enumerate(filtered_habits, start=1):
                        print(f"{count}. {habit['Task']}: {habit['Specification']} - created at: {habit['Start_Date']}")

                    # pprint(filtered_habits, width=60, depth=30, compact=True)

                    def habits_weekly(x):
                        """This function sorted out the activ habits with weekly periodicity"""
                        return x['Periodicity'] == 'weekly' and x['Active']  # == True

                    filtered_habits = tuple(filter(habits_weekly, habits_tuple))
                    print('\nPeriodicity: weekly\n')
                    for count, habit in enumerate(filtered_habits, start=1):
                        print(f"{count}. {habit['Task']}: {habit['Specification']} - created at: {habit['Start_Date']}")
                    # pprint(filtered_habits, width=60, depth=30, compact=True)
                    input('\n_________________________________________\n'
                          '\nTo go back press any key.')
                    model.clear_console()

                # list_of_all_currently_tracked_habits_sorted_by_their_periodicity()
                elif user_choice == "2":
                    model.clear_console()
                    try:
                        streak_run = RunStreak()
                        database = 'database.json'
                        streak_run.the_longest_run_streak_for_habits(database)
                    except Exception as e:
                        print("An error occurred:", e)

                elif user_choice == "b":
                    model.clear_console()
                    # menu.main_menu(log_out_file, database)
                    main_menu()

                else:
                    print('Invalid input. Please type "a" or "b".')

            except Exception as e:
                print('An error occurred:', e)

    def the_longest_run_streak_for_habits(self, database):
        """Display the longest run streak for habits.

        Args:
            database (str): The name of the JSON database file.
        """
        model = Utilities()
        habits = model.read_from_json_file(database)
        # menu = menu()
        print('\nThe longest run streak for a single habit is:\n-----------------------------------------------------')

        def run_streak_all(x):
            """Check if a habit's periodicity is either daily or weekly and it is active."""
            return (x['Periodicity'] == 'daily' or x['Periodicity'] == 'weekly') and x['Active']

        filtered_habits = tuple(filter(run_streak_all, habits))

        print('\nPeriodicity: daily\n')

        for habit in filtered_habits:
            if habit['Periodicity'] == 'daily':
                longest_streak, start_date, end_date = self.calculate_longest_streak(habit['Check_offs'],
                                                                                     habit['Periodicity'])
                print(f"{habit['Task']}: Longest streak: {longest_streak} days (from {start_date} to {end_date})")

        print('\nPeriodicity: weekly\n')

        from functionalities.streak_run_weeks import StreakRunWeek
        run_week = StreakRunWeek()
        model = Utilities()
        longest_streak_run_week = run_week.process_weekly_habits(habits)

        filtered_habits = tuple(filter(run_streak_all, habits))

        a = []  # Initialize a list to store tuples

        for habit in filtered_habits:
            longest_streak1, longest_streak_start, longest_streak_end = self.calculate_longest_streak(
                habit['Check_offs'], habit['Periodicity'])
            habit_tuple = (habit['Task'], longest_streak1, longest_streak_start, longest_streak_end)
            a.append(habit_tuple)
        # max_tuple = max(a, key=lambda x: x[1])

        max_tuple = max(a, key=lambda x: x[1])

        # Format the date objects in the tuple
        start_date_formatted = max_tuple[2].strftime('%Y-%m-%d')
        end_date_formatted = max_tuple[3].strftime('%Y-%m-%d')
        longest_streak_run_day = [(max_tuple[0], max_tuple[1], start_date_formatted, end_date_formatted)]
        # print(longest_streak_run_day)
        # print(longest_streak_run_week)

        # Compare both longest_streak_run_ for days and weeks to find max. value
        max_value_list1 = max(longest_streak_run_day, key=lambda x: x[1])[1]
        max_value_list2 = max(longest_streak_run_week, key=lambda x: x[1])[1]

        if max_value_list1 > max_value_list2:
            print(f"The longest streak from all habits is: {longest_streak_run_day[0][1]} days in habit:"
                  f" {longest_streak_run_day[0][0]} from {longest_streak_run_day[0][2]}"
                  f" to {longest_streak_run_day[0][3]}.")
            # print(f"The longest streak from all habits is: {longest_streak_run_day[1]} days from")
        else:
            print(f"The longest streak from all habits is: {longest_streak_run_week[0][1]} days in habit:"
                  f" {longest_streak_run_day[0][0]} in calendar weeks {longest_streak_run_day[0][0]}.")

        input('To go back press any key.')
        model.clear_console()

    @staticmethod
    def calculate_longest_streak(check_offs, periodicity):
        """Calculate the longest streak of completed habits.

        Args:
            check_offs (list): List of completed dates in string format.
            periodicity (str): The periodicity of the habit; "daily" or "weekly".

        Returns:
            tuple: Longest streak length, start date, and end date of the streak.
        """

        sorted_dates = sorted([datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f').date() for date_str in check_offs])

        if periodicity == 'daily':
            streak_threshold = timedelta(days=1)
        else:
            return 0, None, None

        longest_streak = 0
        current_streak = 1
        current_streak_start = sorted_dates[0]

        for i in range(1, len(sorted_dates)):
            if (sorted_dates[i] - sorted_dates[i - 1]) <= streak_threshold:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    longest_streak_start = current_streak_start
                current_streak = 1
                current_streak_start = sorted_dates[i]

        if current_streak > longest_streak:
            longest_streak = current_streak
            longest_streak_start = current_streak_start

        longest_streak_end = longest_streak_start + timedelta(days=longest_streak - 1)
        # print(longest_streak, longest_streak_start, longest_streak_end )

        return longest_streak, longest_streak_start, longest_streak_end
