from utilities.utilities import Utilities
from datetime import datetime, timedelta


class Analytics:
    def __init__(self, habits, main_menu):
        self.habits = habits
        self.main_menu = main_menu

    def analytics(self, habits, main_menu, database):
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
                        '\nThe list of all currently tracked habits sorted by their periodicity.\n')  # "Habits as a
                    # tuple:

                    def habits_daily(x):
                        return x['Periodicity'] == 'daily' and x['Active']  # == True

                    filtered_habits = filtered_habits = tuple(filter(habits_daily, habits_tuple))
                    print('\nPeriodicity: daily\n')
                    for count, habit in enumerate(filtered_habits, start=1):
                        print(f"{count}. {habit['Task']}: {habit['Specification']} - created at: {habit['Start_Date']}")

                    # pprint(filtered_habits, width=60, depth=30, compact=True)

                    def habits_weekly(x):
                        return x['Periodicity'] == 'weekly' and x['Active']  # == True

                    filtered_habits = filtered_habits = tuple(filter(habits_weekly, habits_tuple))
                    print('\nPeriodicity: weekly\n')
                    for count, habit in enumerate(filtered_habits, start=1):
                        print(f"{count}. {habit['Task']}: {habit['Specification']} - created at: {habit['Start_Date']}")
                    # pprint(filtered_habits, width=60, depth=30, compact=True)
                    input('\n_________________________________________\n'
                          '\nTo go back press any key.')
                    model.clear_console()
                    # menu.main_menu(log_out_file, database)()
                    # main_menu()

                # list_of_all_currently_tracked_habits_sorted_by_their_periodicity()
                elif user_choice == "2":
                    model.clear_console()
                    try:
                        self.the_longest_run_streak_for_habits(habits, database)
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

    def the_longest_run_streak_for_habits(self, habits, database):
        model = Utilities()
        habits = model.read_from_json_file(database)
        # menu = menu()
        print('\nThe longest run streak for a single habit is:\n-----------------------------------------------------')

        def run_streak_all(x):
            return (x['Periodicity'] == 'daily' or x['Periodicity'] == 'weekly') and x['Active']

        filtered_habits = tuple(filter(run_streak_all, habits))

        print('\nPeriodicity: daily\n')

        for habit in filtered_habits:
            if habit['Periodicity'] == 'daily':
                longest_streak, start_date, end_date = self.calculate_longest_streak(habit['Check_offs'],
                                                                                     habit['Periodicity'])
                print(f"{habit['Task']}: Longest streak: {longest_streak} days (from {start_date} to {end_date})")

        print('\nPeriodicity: weekly\n')

        for habit in filtered_habits:
            if habit['Periodicity'] == 'weekly':
                longest_streak, start_date, end_date = self.calculate_longest_streak(habit['Check_offs'],
                                                                                     habit['Periodicity'])
                print(f"{habit['Task']}: Longest streak: {longest_streak} weeks (from {start_date} to {end_date})")

        longest_streak_overall = 0
        longest_streak_habit = None

        for habit in filtered_habits:
            longest_streak, _, _ = self.calculate_longest_streak(habit['Check_offs'], habit['Periodicity'])
            if longest_streak > longest_streak_overall:
                longest_streak_overall = longest_streak
                longest_streak_habit = habit['Task']

        print(
            f"\nThe longest streak from all habits: {longest_streak_overall} days in habit: {longest_streak_habit}\n"
            f"--------------------------------------------------------------\n")

        input('To go back press any key.')
        model.clear_console()

    @staticmethod
    def calculate_longest_streak(check_offs, periodicity):
        sorted_dates = sorted([datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f') for date_str in check_offs])

        if periodicity == 'daily':
            streak_threshold = timedelta(days=1)
        else:
            streak_threshold = timedelta(weeks=1)

        longest_streak = 0
        current_streak = 0
        longest_streak_start = None
        current_streak_start = None

        for i in range(1, len(sorted_dates)):
            if (sorted_dates[i] - sorted_dates[i - 1]) <= streak_threshold:
                if current_streak == 0:
                    current_streak_start = sorted_dates[i - 1]
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    longest_streak_start = current_streak_start
                current_streak = 0

        if current_streak > longest_streak:
            longest_streak = current_streak
            longest_streak_start = current_streak_start

        if longest_streak_start:
            longest_streak_end = longest_streak_start + streak_threshold * longest_streak
            return longest_streak, longest_streak_start.date(), longest_streak_end.date()
        else:
            return 0, None, None
