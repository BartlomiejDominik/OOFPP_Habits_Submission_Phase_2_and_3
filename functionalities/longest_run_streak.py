from utilities.utilities import Utilities
from datetime import datetime, timedelta


class RunStreak:
    """This class is used to calculate and display the longest run streak for habits."""

    def the_longest_run_streak_for_habits(self, database):
        model = Utilities()
        model.read_from_json_file(database)
        """Display the longest run streak for habits.

        Args:
            database (str): The name of the JSON database file.
        """
        model = Utilities()
        habits = model.read_from_json_file(database)
        print('\nThe longest run streak for tuple_initialization_list single habit '
              'is:\n-----------------------------------------------------')

        def run_streak_all(x):
            """Check if tuple_initialization_list habit's periodicity is either daily or weekly and it is active."""
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

        longest_streak_run_week = run_week.process_weekly_habits(database)

        filtered_habits = tuple(filter(run_streak_all, habits))

        tuple_initialization_list = []  # Initialize tuple_initialization_list list to store tuples

        for habit in filtered_habits:
            longest_streak1, longest_streak_start, longest_streak_end = self.calculate_longest_streak(
                habit['Check_offs'], habit['Periodicity'])
            habit_tuple = (habit['Task'], longest_streak1, longest_streak_start, longest_streak_end)
            tuple_initialization_list.append(habit_tuple)
        max_tuple = max(tuple_initialization_list, key=lambda x: x[1])

        max_tuple = max(tuple_initialization_list, key=lambda x: x[1])

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
            input('\nTo go back press any key.')
            model.clear_console()
            return longest_streak_run_day[0][1]
        else:
            print(f"The longest streak from all habits is: {longest_streak_run_week[0][1]} weeks in habit:"
                  f" {longest_streak_run_day[0][0]} in calendar weeks {longest_streak_run_day[0][0]}.")
            input('\nTo go back press any key.')
            model.clear_console()
            return longest_streak_run_week[0][1]
        # input('\nTo go back press any key.')
        # model.clear_console()

    @staticmethod
    def calculate_longest_streak(check_offs, periodicity):
        """Calculate the longest streak of completed habits.

        Args:
            check_offs (list): A list of strings representing completed dates in the format '%Y-%m-%dT%H:%M:%S.%f'.
            periodicity (str): The periodicity of the habit; "daily" or "weekly".

        Returns:
            tuple: A tuple containing the longest streak length, start date, and end date of the streak.
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
        # print(longest_streak, longest_streak_start, longest_streak_end)

        return longest_streak, longest_streak_start, longest_streak_end
