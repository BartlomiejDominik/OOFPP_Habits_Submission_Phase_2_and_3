from utilities.utilities import Utilities
from instructions.user_manual import Manual


class HelpNavigation:
    """This class is used to navigate to the user manual."""

    @staticmethod
    def help_navigation(main_menu):
        """Navigate to the user manual for providing help to the user.

        Args:
            main_menu (function): The main menu function to return after help is accessed.
        """
        model = Utilities()
        user_manual = Manual()
        model.clear_console()
        user_manual.user_manual(main_menu)
