import random
from datetime import datetime, timedelta
from habit.modifications import Operations
from utilities.utilities import Utilities


class Set:
    """A class containing methods to generate and manipulate test data for habits.

    Attributes:
        N/A
    """

    @staticmethod
    def test_function(habits, database):
        """
        Generate a random dataset for testing habits over the past 28 days.

        Args:
            habits (list): A list of habit dictionaries.
            database (str): The filename of the JSON database containing habits' data.

        Returns:
            None
        """
        model = Utilities()
        dataset = Set()
        operation = Operations()
        model.clear_console()
        # option61 = Option6()

        while True:
            try:
                model.clear_console()
                user_choice = input(
                    '\nTo generate the random dataset for past 28 days?\n'
                    'Please enter (y) for yes and (n) to go back.\n')
                if user_choice == 'y':
                    model.clear_console()
                    # habits.clear()
                    operation.predefined_habits([], database)  # 'test.json'
                    dataset.random_day(habits, database)
                    for habit in habits:
                        print(habit)
                    input('\nPlease press enter to go forward')
                    break
                elif user_choice == 'n':
                    break

            except Exception as e:
                print('An error occurred:', e)

    @staticmethod
    def random_day(habits, database):
        """Generate random check-off dates for habits over the past 28 days.

        Args:
            habits (list): A list of habit dictionaries.
            database (str): The filename of the JSON database containing habits' data.

        Returns:
            list: Updated list of habit dictionaries with random check-off dates.
        """
        model = Utilities()
        model.clear_console()
        dataset = Set()
        num_days = 28

        for habit in habits:
            check_off_dates = set()

            for _ in range(num_days):
                if habit['Periodicity'] == "daily":
                    if random.random() < 0.85:
                        random_hour = random.randint(0, 23)
                        random_minute = random.randint(0, 59)
                        random_second = random.randint(0, 59)
                        random_microsecond = random.randint(0, 999999)
                        check_off_date = datetime.now() - timedelta(days=random.randint(0, num_days),
                                                                    hours=random_hour,
                                                                    minutes=random_minute,
                                                                    seconds=random_second,
                                                                    microseconds=random_microsecond)
                        check_off_dates.add(check_off_date.strftime('%Y-%m-%dT%H:%M:%S.%f'))
                elif habit['Periodicity'] == "weekly":
                    if random.random() < 0.05:
                        random_hour = random.randint(0, 23)
                        random_minute = random.randint(0, 59)
                        random_second = random.randint(0, 59)
                        random_microsecond = random.randint(0, 999999)
                        check_off_date = datetime.now() - timedelta(days=random.randint(0, num_days),
                                                                    hours=random_hour,
                                                                    minutes=random_minute,
                                                                    seconds=random_second,
                                                                    microseconds=random_microsecond)
                        check_off_dates.add(check_off_date.strftime('%Y-%m-%dT%H:%M:%S.%f'))

            habit['Check_offs'] = sorted(list(check_off_dates))

        model.save_into_json_file(habits, database, indent_level=4)
        dataset.remove_duplicates(habits, database)
        print(habits)
        return habits

    @staticmethod
    def remove_duplicates(habits, database):
        """Remove duplicate check-off dates from the habit dictionaries.

        Args:
           habits (list): A list of habit dictionaries.
           database (str): The filename of the JSON database containing habits' data.

        Returns:
           list: Updated list of habit dictionaries with removed duplicate check-off dates.
        """
        from utilities.utilities import Utilities
        from datetime import datetime
        utilities = Utilities()

        # Remove duplicates from the Check_offs list based on yy-mm-dd format
        for habit in habits:
            unique_dates = set()
            new_check_offs = []
            for date_str in habit['Check_offs']:
                date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
                date_yyyymmdd = date.strftime('%Y-%m-%d')
                if date_yyyymmdd not in unique_dates:
                    unique_dates.add(date_yyyymmdd)
                    new_check_offs.append(date_str)
            habit['Check_offs'] = new_check_offs
        utilities.save_into_json_file(habits, database, indent_level=4)
        return habits
        # print(habits)
