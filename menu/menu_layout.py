from habit.modifications import Operations


class Menu:
    @staticmethod
    def menu_layout(log_out_file, database):
        operation = Operations()

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
                                                                "| The following habits have been broken since last "
                                                                "log-in:" + " " * (
                      line - len(text2) - 1) + "|\n"
                                               "|" + " " * (line - 2) + "|\n"
                                                                        "| On daily basis:" + " " * (
                      line - len(text3) - 1) + "|\n"
                                               "|" + " " * (line - 2) + "|")
        operation.list_of_habits_not_being_checked_off_since_last_login("daily", log_out_file, database, line)
        print("|" + " " * (line - 2) + "|\n"
                                       "| On weekly basis:" + " " * (line - len(text4) - 1) + "|\n"
                                                                                              "|" + " " * (
                          line - 2) + "|")
        operation.list_of_habits_not_being_checked_off_since_last_login("weekly", log_out_file, database, line)
        print("|" + "_" * (line - 2) + "|\n"
                                       "|" + " " * (line - 2) + "|\n"
                                                                "| What would you like to do? Please insert one letter "
                                                                "from below:" + " " * (
                      line - len(text5) - 1) + "|\n"
                                               "|" + " " * (line - 2) + "|\n"
                                                                        "| (h)	- to get some help at the beginning."
                    + " " * (
                      line - len(text6) - 3) + "|\n"
                                               "|" + " " * (line - 2) + "|\n"
                                                                        "| (c)	- to check-off an existing habit." + " "
              * (
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
