from utilities.utilities import Utilities


class Manual:
    """A class to provide the user manual and instructions for using the HabiBart App."""
    @staticmethod
    def user_manual(main_menu):
        """Display the user manual and instructions for using the HabiBart App.

        Args:
            main_menu (function): The main menu function to return after reading the manual.

        Returns:
            None
        """
        model = Utilities()
        while True:
            try:
                print('\nHelp for using HabiBart App\n'
                      '\nThank You very much for choosing our habits tracking application, HabiBart.\n'
                      '\n###################################################################################'
                      '\n1. At the beginning you have five predefined habits to choose from. You can deactivate\n'
                      '   any of these habits by going to the setting and selecting the habit you wish to deactivate.\n'
                      '\n 2. To create a new habit, simply choose the "Add new habit" option from the main menu by '
                      'typing (n).\n'
                      '\n 3. To mark a habit as completed, uss the "Check off" option in the menu by typing (c).\n'
                      '\n 4. For viewing analytics of all habits, select the "Analytics" option in the menu by typing '
                      '(a).\n'
                      '###################################################################################\n')

                back = input('To go back to main menu please enter (b):\n')

                if back == "b":
                    model.clear_console()
                    main_menu()
                else:
                    model.clear_console()

            except Exception as e:
                print('An error occurred:', e)
