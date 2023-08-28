import time  # to delay the execution of the functions f.e in main_menu()
from functionalities.analytics import Analytics
from functionalities.close_app import CloseApp
from functionalities.help_navigation import HelpNavigation
from functionalities.add_new_habit import AddNewHabit
from functionalities.settings import Settings
from menu.menu_layout import Menu
from functionalities.habits_check_off import CheckOff
from utilities.utilities import Utilities
from menu.initialisation import StartInitialisation
from unit_test.test_fixture import TestFixture

test_run = TestFixture()
test_run.test_fixture()

habits = []  # a list where all the habits(dictionaries) are aggregated
database = "database.json"  # a name of the file where the 'habits' list is stored
log_out_file = "logout_time.json"  # file to store the logout time
not_completed_habits_day = []  # global variable to store ont completed habits: day
not_completed_habits_week = []  # global variable to store ont completed habits: week


# this function is prepared for launching the App
def start_function():
    initialisation = StartInitialisation()
    initialisation.start_initialisation(database, log_out_file)
    main_menu()
    choose_one_option()


def main_menu():
    menu = Menu()
    menu.menu_layout(log_out_file, database)

    time.sleep(.5)  # to delay the execution of the function
    choose_one_option()


def option2():
    model = Utilities()
    model.clear_console()
    add_new_habit = AddNewHabit()

    # enable user to add a new habit
    add_new_habit.new_habit_add(database, main_menu)


# code written to simulate the menu functions in GUI
def choose_one_option():
    utilities = Utilities()
    analytics = Analytics(habits, main_menu)
    close_app = CloseApp()
    help_navigation = HelpNavigation()
    settings = Settings(habits, main_menu, database, log_out_file)
    check_off = CheckOff()
    user_choice = input("I choose: ")

    if user_choice == "h":
        help_navigation.help_navigation(main_menu)

    if user_choice == "c":
        check_off.daily_and_weekly_habits_function(database, not_completed_habits_day, not_completed_habits_week)
        main_menu()

    elif user_choice == "n":
        option2()

    elif user_choice == "a":
        analytics.analytics(habits, main_menu, database)

    elif user_choice == "x":
        close_app.close_app(log_out_file)
        main_menu()

    elif user_choice == "s":
        settings.settings(habits, main_menu, database, log_out_file)
        settings.settings(habits, main_menu, database, log_out_file)
        settings.settings(habits, main_menu, database, log_out_file)
    elif user_choice == "print":
        for habit in habits:
            print(habit)
    else:
        utilities.clear_console()
        main_menu()
        choose_one_option()


if __name__ == '__main__':
    start_function()
