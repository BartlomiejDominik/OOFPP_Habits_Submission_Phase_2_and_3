from datetime import datetime

from utilities.utilities import Utilities


class StreakRunWeek:

    @staticmethod
    def get_calendar_week(date_str):
        date = datetime.fromisoformat(date_str)
        year, week_num, _ = date.isocalendar()
        return year, week_num

    @staticmethod
    def find_streak_weeks(sorted_list):
        streak_run_weeks = StreakRunWeek()
        streaks = []
        current_streak = [streak_run_weeks.get_calendar_week(sorted_list[0])[1]]

        for i in range(1, len(sorted_list)):
            current_week = streak_run_weeks.get_calendar_week(sorted_list[i])[1]
            previous_week = streak_run_weeks.get_calendar_week(sorted_list[i - 1])[1]

            if current_week == previous_week + 1:
                current_streak.append(current_week)
            else:
                streaks.append(current_streak)
                current_streak = [current_week]

        streaks.append(current_streak)  # Append the last streak

        return [streak for streak in streaks if len(streak) > 1]

    @staticmethod
    def process_weekly_habits(database):
        """Calculate the longest streak of completed habits.

        Args:
            database (str): The name of the JSON database file.

        Returns:
            tuple: A tuple containing the longest weeks streak
        """

        model = Utilities()
        streak_run_weeks = StreakRunWeek()
        # model.read_from_json_file(database)
        habits = model.read_from_json_file(database)
        habit_details = []

        for habit in habits:
            habit_id = habit["Id"]
            task = habit["Task"]
            periodicity = habit["Periodicity"]
            dates = habit["Check_offs"]

            if periodicity == "weekly" and dates:
                habit_details.append((habit_id, task, dates))
        list_of_tasks = []
        longest_streak_all = []

        #year = int(datetime.strptime(model.read_from_json_file('logout_time.json'), '%Y-%m-%d').year)
        for habit_tuple in habit_details:
            habit_id, task, dates = habit_tuple
            list_of_tasks.append(f"{task}, ")
            week_dates = [date for date in dates if
                          streak_run_weeks.get_calendar_week(date)[0] == 2023]  #2023
            sorted_week_dates = sorted(week_dates)
            streak_weeks = streak_run_weeks.find_streak_weeks(sorted_week_dates)

            if streak_weeks:
                max_sublist = max(streak_weeks, key=len)
                print(f"{task}: Longest streak: {len(max_sublist)} weeks in calendar weeks: {max_sublist}")
                # Append the information as a tuple to the 'longest_streak_all' list
                longest_streak_all.append((task, len(max_sublist), max_sublist))
                # Find the tuple(s) with the maximum value from the second position
                max_streak_length = max(longest_streak_all, key=lambda x: x[1])[1]
                max_tuples = [(task, length, weeks) for task, length, weeks in longest_streak_all if
                              length == max_streak_length]

                return max_tuples
