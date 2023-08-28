from utilities.utilities import Utilities
from datetime import datetime, timedelta


class RunStreak:

    def the_longest_run_streak_for_habits(self, habits):
        model = Utilities()
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
