import json  # importing build-in package to work with json data.
import os  # for cleaning the console
from datetime import date, datetime, timedelta  # to import a library for getting a present date
import time  # to delay the execution of the functions f.e in main_menu()
import sys  # for closing the App chosen by user
import random  # to create data for last for weeks

habits = []  # a list where all the habits(dictionaries) are aggregated
database = "database.json"  # a name of the file where the 'habits' list is stored
log_out_file = "logout_time.json"  # file to store the logout time
not_completed_habits_day = []  # global variable to store ont completed habits: day
not_completed_habits_week = []  # global variable to store ont completed habits: week


# logout function to save logout date and exit the code
def log_out():
    log_out_time = datetime.now().date().isoformat()  # .isoformat() converts date into a string(ISO 8601:"YYYY-MM-DD")
    save_into_json_file(log_out_time, log_out_file, indent_level=4)  # indent specifies number of spaces for each
    # level of indentation in *.json file. This makes the structure of the file more readable if open separately.
    sys.exit()  # exit the code


def list_of_habits_not_being_checked_off_since_last_login(periodicity):  # executed with:'daily' or 'weekly' parameter
    last_login = read_from_json_file(log_out_file)  # read from file when user close the app for the last time
    last_login_date = datetime.strptime(last_login, '%Y-%m-%d').date()  # convert a date string in the format
    # 'YYYY-MM-DD' into a date
    today = datetime.now().date()

    habits_not_checked_off = read_from_json_file(database)  # read database from file and store it into new variable
    not_checked_off_habits = []  # create empty list for the further iterations

    for habit in habits_not_checked_off:  # prepared the data in Check_off's list to be used in python
        check_offs = [datetime.fromisoformat(check_off.split("T")[0]).date() for check_off in habit["Check_offs"]]
        if habit["Periodicity"] == periodicity:  # sort out 'habit' dictionaries with 'daily' or 'weekly' periodicity
            for date1 in daterange(last_login_date + timedelta(days=1), today):  # check
                if date1 not in check_offs:
                    # Create a copy of the habit dictionary to avoid modifying the original habit
                    new_habit = habit.copy()
                    new_habit["Missing_Checkoff_Date"] = date1.isoformat()
                    not_checked_off_habits.append(new_habit)
    if periodicity == "daily":
        for habit in not_checked_off_habits:
            print("|", habit['Task'], habit['Specification'], "at", habit['Missing_Checkoff_Date'])
    elif periodicity == "weekly":
        weekly_habit_tasks_printed = set()  # help tracking the printed habits 'Task'
        for habit in not_checked_off_habits:
            if habit['Task'] not in weekly_habit_tasks_printed:
                print("|", habit['Task'], habit['Specification'])
                weekly_habit_tasks_printed.add(habit['Task'])
    return not_checked_off_habits


def daterange(start_date, end_date):  # to generate a sequence of dates within a specified range
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def list_of_habits_to_check_off_today():
    last_login = datetime.now().date().isoformat()
    # print(last_login)
    habits_for_today = read_from_json_file(database)
    # not_completed_habits = []

    global not_completed_habits_day
    not_completed_habits_day.clear()  # clear the variable for the next iteration

    for habit in habits_for_today:

        check_offs = habit["Check_offs"]
        if habit["Periodicity"] == "daily" and not any(
                last_login in check_off.split("T")[0] for check_off in check_offs):
            # (last_login in check_off.split("T")[0] for check_off in check_offs)
            not_completed_habits_day.append(habit)
    return not_completed_habits_day


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_start_and_end_of_week():
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
    end_of_week = start_of_week + timedelta(days=6)  # Sunday of the current week
    return start_of_week, end_of_week


def list_of_weekly_habits_with_check_offs_this_week():
    start_of_week, end_of_week = get_start_and_end_of_week()
    # print("Start of Week:", start_of_week)
    # print("End of Week:", end_of_week)

    habits_for_this_week = read_from_json_file(database)

    global not_completed_habits_week
    not_completed_habits_week.clear()

    for habit in habits_for_this_week:
        check_offs = habit["Check_offs"]
        if habit["Periodicity"] == "weekly":
            if not check_offs or not any(
                    start_of_week <= datetime.fromisoformat(check_off.split("T")[0]).date() <= end_of_week for check_off
                    in check_offs):
                not_completed_habits_week.append(habit)
    # print(not_completed_habits_week)
    return not_completed_habits_week


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Class based on json bibliothek create to prepare the dates to be saved in json format.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)


# Function for saving databank in json file based on a EncoderClass
def save_into_json_file(data, filename, indent_level=2):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=indent_level, cls=CustomJSONEncoder)


# Function for reading from data with dates from json file
def read_from_json_file(filename):
    # try:
    with open(filename, "r") as read_file:
        data = json.load(read_file, object_hook=date_hook)
        return data


# Function for converting the data from a json file back to the dates format
def date_hook(obj_dict):
    for key, value in obj_dict.items():
        if isinstance(value, str):
            try:
                # Check if the value is in ISO date format and convert it to a date object
                obj_dict[key] = date.fromisoformat(value)
            except ValueError:
                pass
    return obj_dict


# Class prepared for adding a new habits
class Habit:

    def __init__(self, task, specification, periodicity):
        self.task = task
        self.specification = specification
        self.periodicity = periodicity

    def set_new_habit(self):
        start_date = datetime.now().date()
        id_number = max((habit['Id'] for habit in habits), default=0) + 1

        return {'Id': id_number, 'Task': self.task, 'Specification': self.specification,
                'Periodicity': self.periodicity, 'Active': True, 'Start_Date': start_date, 'Check_offs': []}


# this function is prepared for launching the App
def start_function():
    global habits
    # Checking if the file exist
    try:
        habits = read_from_json_file(database)  # "database(*).json"
        # main_menu()

    except FileNotFoundError:
        # If the file doesn't exist, create it with an empty "habits" list and fill it with predefined_habits()
        habits = []
        print("\nError: Database hasn't existed yet or the App wasn't able to open the existing file.\n"
              "For that reason the database was created with following, default habits.\n")
        predefined_habits()
        input("\nPress any key to go forward to main menu.")
        clear_console()
    # checking if the logout_time file exist and if not creat a new one with the last logout date set to two days
    # before for testing purpose
    try:
        read_from_json_file(log_out_file)  # "database(*).json"
    #     main_menu()
    #
    except FileNotFoundError:
        # If the file doesn't exist, create a new with the logout time set two day before for testing not completed
        # habits since last login
        log_out_time = (datetime.now().date() - timedelta(days=2)).isoformat()  # .isoformat() converts date into a
        # string(ISO8601:"YYYY-MM-DD")
        save_into_json_file(log_out_time, log_out_file, indent_level=4)  # indent specifies number of spaces for each
        # level of indentation in *.json file. This makes the structure of the file more readable if open separately.
        print(f"\nError: Log_out_time file hasn't existed yet or the App wasn't able to open the existing file.\n"
              f"For that reason the new file was created with following date: {log_out_time}\n")
        input("\nPress any key to go forward to main menu.")
        clear_console()
        # main_menu()
    main_menu()


# code written to simulate the menu functions in GUI
def main_menu():
    line = 76
    text1 = '| Welcome to HabiBart App!!!'
    text2 = '| The following habits have been broken since last log-in:'
    text3 = '| On daily basis:'
    text4 = '| On weekly basis:'
    text5 = '| What would you like to do? Please insert one letter from below:'
    text6 = '| (h)	- to get some help at the beginning.'
    text7 = '| (c)	- to check-off an existing habit.'
    text8 = '| (n)	- to create a new habit.'
    text9 = '| (a)	- to see the analytics.'
    text10 = '| (s) 	- to enter the settings.'
    text11 = '| (x) 	- to quit.'
    print("\n" + "*" * line)
    print("| Welcome to HabiBart App!!!" + " " * (line - len(text1) - 1) + "|")
    print("|" + "_" * (line - 2) + "|\n"
                                   "|" + " " * (line - 2) + "|\n"
                                                            "| The following habits have been broken since last log-in:" + " " * (
                  line - len(text2) - 1) + "|\n"
                                           "|" + " " * (line - 2) + "|\n"
                                                                    "| On daily basis:" + " " * (
                  line - len(text3) - 1) + "|\n"
                                           "|" + " " * (line - 2) + "|")
    list_of_habits_not_being_checked_off_since_last_login("daily")
    print("|" + " " * (line - 2) + "|\n"
                                   "| On weekly basis:" + " " * (line - len(text4) - 1) + "|\n"
                                                                                          "|" + " " * (line - 2) + "|")
    list_of_habits_not_being_checked_off_since_last_login("weekly")
    print("|" + "_" * (line - 2) + "|\n"
                                   "|" + " " * (line - 2) + "|\n"
                                                            "| What would you like to do? Please insert one letter "
                                                            "from below:" + " " * (
                  line - len(text5) - 1) + "|\n"
                                           "|" + " " * (line - 2) + "|\n"
                                                                    "| (h)	- to get some help at the beginning." + " " * (
                  line - len(text6) - 3) + "|\n"
                                           "|" + " " * (line - 2) + "|\n"
                                                                    "| (c)	- to check-off an existing habit." + " " * (
                  line - len(text7) - 3) + "|\n"
                                           "| (n)	- to create a new habit." + " " * (
                  line - len(text8) - 3) + "|\n"
                                           "| (a)	- to see the analytics." + " " * (
                  line - len(text9) - 3) + "|\n"
                                           "|" + " " * (line - 2) + "|\n"
                                                                    "| (s) 	- to enter the settings." + " " * (
                  line - len(text10) - 2) + "|\n"
                                            "| (x) 	- to quit." + " " * (line - len(text11) - 2) + "|")
    print("*" * line)
    time.sleep(.5)  # to delay the execution of the function
    choose_one_option()


# Creat a list of default habits with the Habit Class
def predefined_habits():
    habit = Habit("Jogging", "At least 30 min. or 3 KM.", "daily")
    habits.append(habit.set_new_habit())

    habit = Habit("Reading", "At least one book a week.", "weekly")
    habits.append(habit.set_new_habit())

    habit = Habit("Learning", "At least one new foreign word a day", "daily")
    habits.append(habit.set_new_habit())

    habit = Habit("Eating", "At least 200g vegetables per day.", "daily")
    habits.append(habit.set_new_habit())

    habit = Habit("Education", "Visit to a museum or theater once a week.", "weekly")
    habits.append(habit.set_new_habit())

    save_into_json_file(habits, database, indent_level=4)  # "database(*).json"

    for habit in habits:
        print(habit)  # print each item from the list in a separate line


# this function clear the console to make the App easier to use
def clear_console():
    # Check the platform and execute the appropriate clear command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')


def option1():
    # search in a 'habits' database and print all the habits that have to be done daily
    print('\nHabits on a daily basis:\n')
    counter = 0
    max_counter = 0
    # chosen_habit = 0
    daily_and_weekly_habits = []  # a new empty list to store habits from 'habits' database sorted by periodicity:
    # daily, weekly
    list_of_habits_to_check_off_today()
    # print(not_completed_habits_day)
    # search in a 'habits' database and print all the habits that have to be done daily
    for habit in not_completed_habits_day:  # habits
        if habit['Periodicity'] == "daily":
            counter += 1
            daily_and_weekly_habits.append(habit)
            print(counter, habit['Task'], habit['Start_Date'])  # print each item from the list in a separate line
            max_counter = counter  # Update the maximum index
        else:
            pass

    list_of_weekly_habits_with_check_offs_this_week()
    # search in a 'habits' database and print all the habits that have to be done weekly
    print('------------------------------\nHabits on a weekly basis:\n')
    for habit in not_completed_habits_week:  # habits
        if habit['Periodicity'] == "weekly":
            max_counter += 1
            daily_and_weekly_habits.append(habit)
            print(max_counter, habit['Task'], habit['Start_Date'], habit['Id'])  # print each item from the list
        # in a separate line
        else:
            pass

    if len(daily_and_weekly_habits) == 0:
        clear_console()
        print(
            '\nCongratulations there are no habits to check off for today!!!\nPlease come back tomorrow or go back to '
            'the main menu to create a new habit.\n')
        input('Press any key to go back to main menu.')
        clear_console()
        main_menu()
    else:
        # for habit in daily_and_weekly_habits:
        # print(habit)  # print each item from the list in a separate line
        while True:
            chosen_habit = input(
                '\nChoose a habit for check-off by entering the number from the list above or (b) to go back '
                'to main menu: ')
            if chosen_habit == 'b':
                clear_console()
                main_menu()
            else:
                try:
                    chosen_habit = int(chosen_habit)
                    if chosen_habit <= max_counter:
                        current_habit = (daily_and_weekly_habits[int(chosen_habit) - 1])
                        keys_to_access = ['Id', 'Task', 'Specification']
                        values = [current_habit[key] for key in keys_to_access]
                        clear_console()
                        # print(f"\n{values} ")

                        while True:
                            print(f"\n{values} ")
                            insert1 = input('\nWould you like to check-off this habit for today or for this week?\n'
                                            '\nPlease insert: (y) - for yes, or (n) - for no: \n')
                            if insert1 == 'n':
                                clear_console()
                                option1()

                            elif insert1 == 'y':
                                # this part of code is looking for the id of the chosen habit in a database.
                                target_id = current_habit['Id']
                                # found_habit = None if not work remove #

                                for habit in habits:
                                    if habit['Id'] == target_id:
                                        check_off = datetime.now()
                                        found_habit = habit
                                        found_habit['Check_offs'].append(check_off)
                                        print(f"This habit was checked_off\n{found_habit}")
                                        save_into_json_file(habits, database,
                                                            indent_level=4)
                                        break  # to save the check-off in database
                                break
                                # for habit1 in habits:
                                # print(habit1)  # print each item from the list in a separate line

                                # print(check_off)

                            else:
                                print('\nIncorrect value. Please insert a correct value."else"')
                                time.sleep(.5)
                                clear_console()

                    else:
                        print('\nInvalid number. Please choose a valid habit number.')

                except ValueError:
                    print('\nIncorrect value. Please and insert a correct value."Error"')
                    time.sleep(.8)
                    clear_console()
            clear_console()
            option1()

            check_off = datetime.now()
            print(type(check_off))  # check how to find a type of this data.
            clear_console()
            option1()
            # main_menu()

            # "check-off an existing habit", with this function user can check-off one from the existing habits.


def option2():
    clear_console()

    # enable user to add a new habit
    option2_new_habit()


def option2_new_habit():
    global habits
    print('\nTo add a new habit please enter the following information.\n'
          '\nTo brake and go back to main menu enter (b)\n')
    new_habit_task = input('Please insert short task description for the new habit: ')
    while not new_habit_task:  # to check if input() in empty
        clear_console()
        option2_new_habit()
    if new_habit_task == 'b':
        clear_console()
        main_menu()
    new_habit_specification = input('Please insert the specification of the new habit: ')
    new_habit_periodicity = input('Please input periodicity; "w" for weakly or "d" for daily: ')

    while new_habit_periodicity != "w" and new_habit_periodicity != "d":
        print('Incorrect input! Please input periodicity; "w" for weekly or "d" for daily: ')
        new_habit_periodicity = input('Please input periodicity; "w" for weakly or "d" for daily: ')

    if new_habit_periodicity == 'w':
        new_habit_periodicity = 'weekly'
    elif new_habit_periodicity == "d":
        new_habit_periodicity = 'daily'

    habit = Habit(new_habit_task, new_habit_specification, new_habit_periodicity)
    habits.append(habit.set_new_habit())
    save_into_json_file(habits, database, indent_level=4)  # "database9.json"
    # for habit in habits:
    # habit  # is needed to print a habit as a 'str' without this changes in Habit-Class are needed

    print('\nNew habit was added to the database\n')
    print(habit)
    time.sleep(3)
    clear_console()
    main_menu()


def option3():
    clear_console()
    # from pprint import pprint
    print(
        '\nAvailable analytics:\n'
        '\n1. The list of all currently tracked habits sorted by their periodicity.\n'
        '\n2. The longest run streak for habits.\n')
    user_choice = input('Please choose the number from the list above or (m) for menu: ')
    if user_choice == "1":
        habits_tuple = tuple(habits)  # The tuple() constructor is used to create a tuple from the list
        clear_console()
        print('\nThe list of all currently tracked habits sorted by their periodicity.\n')  # "Habits as a tuple:

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
        clear_console()
        main_menu()

    # list_of_all_currently_tracked_habits_sorted_by_their_periodicity()
    elif user_choice == "2":
        clear_console()
        try:
            the_longest_run_streak_for_habits()
        except Exception as e:
            print("An error occurred:", e)

    elif user_choice == "m":
        clear_console()
        main_menu()
    else:
        option3()


def option4():
    # print("Option 4")
    if input('\nFor closing the Application please type (y) and any other letter to go back to the menu: \n') == 'y':
        log_out()
    else:
        clear_console()
        main_menu()


def option5():
    clear_console()
    print('\nHelp for using HabiBart App\n'
          '\nThe text will be added.\n')
    back = input('To go back to main menu please enter (b):\n')
    if back == "b":
        clear_console()
        main_menu()
    else:
        option5()


# this part is to creat an external *.json text file and change it with existing database to enable work with analytics
def option6():
    clear_console()
    user_choice = input('\nPlease choose one option from the list:\n'
                        '\n1. Generating test data set for text_fixture\n'
                        '\n2. Deactivate existing habit\n'
                        '\n3. To manually set the last login date for testing purpose.\n')
    if user_choice == '1':
        clear_console()
        test_function()
    elif user_choice == '2':
        clear_console()
        print('\nTo deactivate one of the active habits, please type the number from the list and press "enter":\n')
        counter = 0
        active_habits = []

        for habit in habits:
            if habit['Active']:
                counter += 1
                active_habits.append(habit)
                print(counter, habit['Task'], habit['Start_Date'])

        if active_habits:
            user_choice = input(
                '\nPlease enter the number from the list above (or press Enter to continue without deactivating): ')

            if user_choice.isdigit():
                choice_index = int(user_choice) - 1
                if 0 <= choice_index < len(active_habits):
                    selected_habit = active_habits[choice_index]
                    selected_habit['Active'] = False
                    print(f"You've deactivated the habit: {selected_habit['Task']}")
                else:
                    print("Invalid choice. No habit was deactivated.")
            else:
                print("Continuing without deactivating any habit.")
        else:
            print("No active habits to deactivate.")

        # main_menu()

    elif user_choice == '3':
        clear_console()
        main_menu()
    else:
        option6()


def choose_one_option():
    option = input("I choose: ")

    if option == "h":
        option5()

    if option == "c":
        clear_console()
        option1()

    elif option == "n":
        option2()

    elif option == "a":
        option3()

    elif option == "x":
        option4()

    elif option == "s":
        option6()

    elif option == "print":
        for habit in habits:
            print(habit)
    else:
        print("\nPlease choose a valid option")
        time.sleep(.5)
        clear_console()
        main_menu()
        time.sleep(.2)
        choose_one_option()


def list_of_all_currently_tracked_habits_sorted_by_their_periodicity():
    clear_console()
    all_active_habits = []
    counter = 0
    print('\nThose are all tracked habits sorted by their periodicity:\n'
          '\nDaily:\n')
    all_habits = read_from_json_file(database)
    # print(all_habits)
    for habit1 in all_habits:
        if habit1['Active']:  # and habit1['Periodicity'] == 'daily':  # and habit['Periodicity'] == 'daily':  # if
            # habit[
            # 'Active'] == True -> Boolean
            all_active_habits.append(habit1)
    for habit in all_active_habits:
        if habit['Periodicity'] == 'daily':
            counter += 1
            print(counter, ".", habit['Task'], "-", habit['Specification'], "-", "created at: ", habit['Start_Date'],
                  habit['Periodicity'])
    print('\nWeekly:\n')

    for habit in all_active_habits:
        if habit['Periodicity'] == 'weekly':
            counter += 1
            print(counter, ".", habit['Task'], "-", habit['Specification'], "-", "created at: ", habit['Start_Date'],
                  habit['Periodicity'])

    user_input = input('\nPress (b) to go back or (m) to go to main_menu:\n')
    if user_input == "b":
        option3()
    elif user_input == "m":
        clear_console()
        main_menu()
    else:
        list_of_all_currently_tracked_habits_sorted_by_their_periodicity()


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


def the_longest_run_streak_for_habits():
    print('\nThe longest run streak for a single habit is:\n-----------------------------------------------------')

    def run_streak_all(x):
        return (x['Periodicity'] == 'daily' or x['Periodicity'] == 'weekly') and x['Active']

    filtered_habits = tuple(filter(run_streak_all, habits))

    print('\nPeriodicity: daily\n')

    for habit in filtered_habits:
        if habit['Periodicity'] == 'daily':
            longest_streak, start_date, end_date = calculate_longest_streak(habit['Check_offs'], habit['Periodicity'])
            print(f"{habit['Task']}: Longest streak: {longest_streak} days (from {start_date} to {end_date})")

    print('\nPeriodicity: weekly\n')

    for habit in filtered_habits:
        if habit['Periodicity'] == 'weekly':
            longest_streak, start_date, end_date = calculate_longest_streak(habit['Check_offs'], habit['Periodicity'])
            print(f"{habit['Task']}: Longest streak: {longest_streak} weeks (from {start_date} to {end_date})")

    # if input('What to do now? Press "t" to find the longest streak from all habits: ') == 't':
    longest_streak_overall = 0
    longest_streak_habit = None

    for habit in filtered_habits:
        longest_streak, _, _ = calculate_longest_streak(habit['Check_offs'], habit['Periodicity'])
        if longest_streak > longest_streak_overall:
            longest_streak_overall = longest_streak
            longest_streak_habit = habit['Task']

    print(
        f"\nThe longest streak from all habits: {longest_streak_overall} days in habit: {longest_streak_habit}\n"
        f"--------------------------------------------------------------\n")

    input('Please enter any key to go to main menu.')
    clear_console()
    main_menu()


# this function prepare a list of randomly check-offs for the habits from database.
def test_function():
    clear_console()
    user_choice = input(
        "\nTo generate the random dataset for past 28 days?\nPlease enter (y) for yes and (n) to go back.")
    if user_choice == 'y':
        habits.clear()
        predefined_habits()
        clear_console()
        random_day()
    elif user_choice == 'n':
        clear_console()
        option6()
    else:
        clear_console()
        test_function()


# this part of the code is to creat the set of random check-off for existing habits for last 28 days


def random_day():
    num_days = 30
    clear_console()

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
                if random.random() < 0.1:
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

    save_into_json_file(habits, 'test.json', indent_level=4)
    clear_console()
    print('\nThe list of randomly created check-offs for all habits\n')
    for habit in habits:
        print(habit, "\n")
    input('\nThis dataset is saved as "test.json" file in main folder.\nTo go back please press any key.')
    clear_console()
    option6()


# ------------------------------------------------------------------------------------
# Under is the list of functions to test how the code is working.

# main_menu()
# predefined_habits()
# option2()
# option1()
# list_of_habits_to_check_off_today()
# list_of_weekly_habits_with_check_offs_this_week()
# list_of_habits_not_being_check_off_since_last_login()
# list_of_all_currently_tracked_habits_sorted_by_their_periodicity()
# option6()
start_function()
