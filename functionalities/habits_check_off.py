from utilities.utilities import Utilities
from datetime import datetime
import time
from habit.modifications import Operations


class CheckOff:

    @staticmethod
    def daily_and_weekly_habits_function(database, not_completed_habits_day, not_completed_habits_week):
        model = Utilities()
        habits = model.read_from_json_file(database)
        operation = Operations()

        model.clear_console()
        while True:
            try:
                print('\nHabits on a daily basis:\n')
                counter = 0
                max_counter = 0
                # chosen_habit = 0
                daily_and_weekly_habits = []  # a new empty list to store habits from 'habits' database sorted by
                # periodicity: daily or weekly
                operation.list_of_habits_to_check_off_today(database, not_completed_habits_day)
                # print(not_completed_habits_day)
                # search in a 'habits' database and print all the habits that have to be done daily
                for habit in not_completed_habits_day:  # habits
                    if habit['Periodicity'] == "daily" and habit['Active'] == True:
                        counter += 1
                        daily_and_weekly_habits.append(habit)
                        print(counter, habit['Task'], "-", habit['Specification'])  # print each item from the list
                        # in a separate line
                        max_counter = counter  # Update the maximum index
                    else:
                        pass

                operation.list_of_weekly_habits_with_check_offs_this_week(database, not_completed_habits_week)
                # search in a 'habits' database and print all the habits that have to be done weekly
                print('------------------------------\nHabits on a weekly basis:\n')
                for habit in not_completed_habits_week:  # habits
                    if habit['Periodicity'] == "weekly" and habit['Active'] == True:
                        max_counter += 1
                        daily_and_weekly_habits.append(habit)
                        print(max_counter, habit['Task'], "-", habit['Specification'])  # print each item from the list
                    # in a separate line
                    else:
                        pass

                while True:
                    try:
                        if len(daily_and_weekly_habits) == 0:
                            model.clear_console()
                            print(
                                '\nCongratulations there are no habits to check off for today!!!\nPlease come back '
                                'tomorrow or go back to the main menu to create a new habit.\n')
                            input('Press any key to go back to main menu.')
                            model.clear_console()
                            return
                        else:
                            while True:
                                chosen_habit = input(
                                    '\nChoose a habit for check-off by entering the number from the list above or (b) '
                                    'to go back to main menu: ')
                                if chosen_habit == 'b':
                                    model.clear_console()
                                    return
                                else:
                                    try:
                                        chosen_habit = int(chosen_habit)
                                        if chosen_habit <= max_counter:
                                            current_habit = (daily_and_weekly_habits[int(chosen_habit) - 1])
                                            keys_to_access = ['Id', 'Task', 'Specification']
                                            values = [current_habit[key] for key in keys_to_access]
                                            model.clear_console()
                                            while True:
                                                try:
                                                    print(f"\n{values} ")
                                                    insert1 = input('\nWould you like to check-off this habit for '
                                                                    'today or for this week?\n'
                                                                    '\nPlease insert: (y) - for yes, or (n) - for no: '
                                                                    '\n')
                                                    if insert1 == 'n':
                                                        break
                                                    elif insert1 == 'y':
                                                        # this part of code is looking for id of the chosen habit
                                                        # in a database.
                                                        target_id = current_habit['Id']
                                                        # found_habit = None if not work remove #

                                                        for habit in habits:
                                                            if habit['Id'] == target_id:
                                                                check_off = datetime.now()
                                                                found_habit = habit
                                                                found_habit['Check_offs'].append(check_off)
                                                                model.save_into_json_file(habits, database,
                                                                                          indent_level=4)
                                                                print(f"This habit was checked_off\n{found_habit}")
                                                                break  # to save the check-off in database
                                                        break
                                                    else:
                                                        print('\nIncorrect value. Please insert a correct value."else"')
                                                        time.sleep(.5)
                                                        model.clear_console()
                                                except Exception as e:
                                                    print('An error occurred:', e)

                                        else:
                                            print('\nInvalid number. Please choose a valid habit number.')

                                    except ValueError:
                                        print('\nIncorrect value. Please and insert a correct value."Error"')
                                        time.sleep(.8)
                                        model.clear_console()
                                        break
                                model.clear_console()
                                # option1()
                                pass

                                check_off = datetime.now()
                                print(type(check_off))  # check how to find a type of this data.
                                model.clear_console()
                                break
                            pass  # option1()
                        break  # main_menu()

                        # "check-off an existing habit", with this function user can check-off one from the existing
                        # habits.
                    except Exception as e:
                        print('An error occurred:', e)
            except Exception as e:
                print('An error occurred:', e)

    @staticmethod
    def check_off_habit(habit, habits, database):
        model = Utilities()
        check_off = datetime.now()
        found_habit = habit
        found_habit['Check_offs'].append(check_off)
        model.save_into_json_file(habits, database,
                                  indent_level=4)
        return habits
