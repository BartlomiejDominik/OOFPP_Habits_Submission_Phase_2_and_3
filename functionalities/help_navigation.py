from utilities.utilities import Utilities
from instructions.user_manual import Manual


class HelpNavigation:

    @staticmethod
    def help_navigation(main_menu):
        model = Utilities()
        user_manual = Manual()
        model.clear_console()
        user_manual.user_manual(main_menu)
