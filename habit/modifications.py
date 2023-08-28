from habit.habit import Habit
from utilities.utilities import Utilities
from datetime import timedelta, datetime


class Operations:

    @staticmethod
    def predefined_habits(habits, database):
        model = Utilities()

        habit = Habit("Jogging", "At least 30 min. or 3 KM.", "daily", habits)
        habits.append(habit.set_new_habit())

        habit = Habit("Reading", "At least one book a week.", "weekly", habits)
        habits.append(habit.set_new_habit())

        habit = Habit("Learning", "At least one new foreign word a day", "daily", habits)
        habits.append(habit.set_new_habit())

        habit = Habit("Eating", "At least 200g vegetables per day.", "daily", habits)
        habits.append(habit.set_new_habit())

        habit = Habit("Education", "Visit to a museum or theater once a week.", "weekly", habits)
        habits.append(habit.set_new_habit())

        model.save_into_json_file(habits, database, indent_level=4)  # "database(*).json"

        return habits  # unindented by one level

    # executed with: 'daily' or 'weekly' parameter
    def list_of_habits_not_being_checked_off_since_last_login(self, periodicity, log_out_file, database, line):
        model = Utilities()
        last_login = model.read_from_json_file(log_out_file)  # read from a file when the user closes the app for
        # last time
        last_login_date = datetime.strptime(last_login, '%Y-%m-%d').date()  # convert a date string in the format
        # 'YYYY-MM-DD' into a date
        today = datetime.now().date()

        habits_not_checked_off = model.read_from_json_file(
            database)  # read the database from file and store it into new variable
        not_checked_off_habits = []  # create an empty list for the further iterations

        for habit in habits_not_checked_off:  # prepared the data in Check_off's list to be used in python
            check_offs = [datetime.fromisoformat(check_off.split("T")[0]).date() for check_off in habit["Check_offs"]]
            if habit["Periodicity"] == periodicity and habit['Active'] == True:  # sort out 'habit' dictionaries with
                # 'daily' or 'weekly'
                # periodicity
                for date1 in self.daterange(last_login_date + timedelta(days=1), today):  # check
                    if date1 not in check_offs:
                        # Create a copy of the habit dictionary to avoid modifying the original habit
                        new_habit = habit.copy()
                        new_habit["Missing_Checkoff_Date"] = date1.isoformat()
                        not_checked_off_habits.append(new_habit)
        if periodicity == "daily":
            for habit in not_checked_off_habits:
                formatted_string = "| {} {} at {} |".format(
                    habit['Task'],
                    habit['Specification'],
                    habit['Missing_Checkoff_Date']
                )

                length_of_formatted_string = len(formatted_string)

                print("|", habit['Task'], habit['Specification'], "at", habit['Missing_Checkoff_Date'],
                      " "*(line-length_of_formatted_string-1), "|")
        elif periodicity == "weekly":
            weekly_habit_tasks_printed = set()  # help tracking the printed habits 'Task'
            for habit in not_checked_off_habits:
                if habit['Task'] not in weekly_habit_tasks_printed:
                    formatted_string = "| {} {} |".format(
                        habit['Task'],
                        habit['Specification']
                    )

                    length_of_formatted_string = len(formatted_string)
                    print("|", habit['Task'], habit['Specification'], " "*(line-length_of_formatted_string-1), "|")
                    weekly_habit_tasks_printed.add(habit['Task'])
        return not_checked_off_habits

    @staticmethod
    def daterange(start_date, end_date):  # to generate a sequence of dates within a specified range
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    # prepare the list of the habits for check-off today

    @staticmethod
    def list_of_habits_to_check_off_today(database, not_completed_habits_day):
        model = Utilities()
        last_login = datetime.now().date().isoformat()
        # print(last_login)
        habits_for_today = model.read_from_json_file(database)
        # not_completed_habits = []

        # global not_completed_habits_day
        not_completed_habits_day.clear()  # clear the variable for the next iteration

        for habit in habits_for_today:

            check_offs = habit["Check_offs"]
            if habit["Periodicity"] == "daily" and not any(
                    last_login in check_off.split("T")[0] for check_off in check_offs):
                # (last_login in check_off.split("T")[0] for check_off in check_offs)
                not_completed_habits_day.append(habit)
        return not_completed_habits_day

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @staticmethod
    def get_start_and_end_of_week():
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
        end_of_week = start_of_week + timedelta(days=6)  # Sunday of the current week
        return start_of_week, end_of_week

    def list_of_weekly_habits_with_check_offs_this_week(self, database, not_completed_habits_week):
        model = Utilities()
        start_of_week, end_of_week = self.get_start_and_end_of_week()

        habits_for_this_week = model.read_from_json_file(database)

        not_completed_habits_week.clear()

        for habit in habits_for_this_week:
            check_offs = habit["Check_offs"]
            if habit["Periodicity"] == "weekly":
                if not check_offs or not any(
                        start_of_week <= datetime.fromisoformat(check_off.split("T")[0]).date() <= end_of_week for
                        check_off
                        in check_offs):
                    not_completed_habits_week.append(habit)
        # print(not_completed_habits_week)
        return not_completed_habits_week
