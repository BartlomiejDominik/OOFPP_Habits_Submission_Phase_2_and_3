from utilities.utilities import Utilities


class CloseApp:
    """This class is used to close the app."""

    @staticmethod
    def close_app(log_out_file):
        """Close the application and log out the user if confirmed by the user.

        Args:
            log_out_file (str): The name of the JSON file for logging out.
        """
        model = Utilities()
        while True:
            try:
                model.clear_console()
                if input('\nTo close the Application please type (y) or press enter to go back to the menu: \n') == 'y':
                    model.log_out(log_out_file)
                else:
                    model.clear_console()
                    break
            except Exception as e:
                print('An error occurred:', e)
